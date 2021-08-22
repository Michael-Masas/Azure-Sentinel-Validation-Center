import logging
import requests
import hashlib
import hmac
import base64
import json
import datetime
import os
from .usecase import Conditional, Default, MFAdisabled1, MFAdisabled2, MultiRDP, UnAuthAADPS, PScmdlets
import azure.functions as func


def get_file_by_name(name="default"):
    return {
        "default": Default,
        "conditional": Conditional,
        "mfadisabled1": MFAdisabled1,
        "mfadisabled2": MFAdisabled2,
        "multirdp": MultiRDP,
        "unauthaadps": UnAuthAADPS,
        "pscmdlets": PScmdlets
    }.get(name)


def build_signature(
    customer_id, shared_key, date, content_length, method, content_type, resource
):
    """Returns authorization header which will be used when sending data into Azure Log Analytics"""

    x_headers = "x-ms-date:" + date
    string_to_hash = (
        method
        + "\n"
        + str(content_length)
        + "\n"
        + content_type
        + "\n"
        + x_headers
        + "\n"
        + resource
    )
    bytes_to_hash = bytes(string_to_hash, "UTF-8")
    decoded_key = base64.b64decode(shared_key)
    encoded_hash = base64.b64encode(
        hmac.new(decoded_key, bytes_to_hash, digestmod=hashlib.sha256).digest()
    ).decode("utf-8")
    authorization = "SharedKey {}:{}".format(customer_id, encoded_hash)
    return authorization


def post_data(customer_id, shared_key, body, log_type):
    """Sends payload to Azure Log Analytics Workspace

    Keyword arguments:
    customer_id -- Workspace ID obtained from Advanced Settings
    shared_key -- Authorization header, created using build_signature
    body -- payload to send to Azure Log Analytics
    log_type -- Azure Log Analytics table name
    """

    method = "POST"
    content_type = "application/json"
    resource = "/api/logs"
    rfc1123date = datetime.datetime.utcnow().strftime("%a, %d %b %Y %H:%M:%S GMT")
    content_length = len(body)
    signature = build_signature(
        customer_id,
        shared_key,
        rfc1123date,
        content_length,
        method,
        content_type,
        resource,
    )
    logging.info("Sig built")
    uri = (
        "https://"
        + customer_id
        + ".ods.opinsights.azure.com"
        + resource
        + "?api-version=2016-04-01"
    )
    logging.info(uri)
    headers = {
        "content-type": content_type,
        "Authorization": signature,
        "Log-Type": log_type,
        "x-ms-date": rfc1123date,
    }

    response = requests.post(uri, data=body, headers=headers)
    logging.info(type(response))
    logging.info(response)
    if response.status_code >= 200 and response.status_code <= 299:
        logging.info("Accepted payload:" + body)
    else:
        logging.error("Unable to Write: " + format(response.status_code))


def main(req: func.HttpRequest, msg: func.Out[str]) -> func.HttpResponse:
    # Get the setting named 'UseCase in Configuration -> Application Settings'
    logging.info("going to main")
    input_msg = "<create the message body required by function 200>"
    msg.set(input_msg)
    usecase_parameter = req.params.get('name')
    if usecase_parameter:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            usecase_parameter = req_body.get('name')
    
    json_dict = get_file_by_name(usecase_parameter)
    if json_dict:
        json_data = json_dict.data
    else:
        return func.HttpResponse(f"UseCase Not Found: {usecase_parameter}", status_code=404)
    
    la_workspace_id = os.environ["WorkspaceID"]
    la_workspace_key = os.environ["WorkspaceKey"]
    azure_log_customer_id = la_workspace_id
    azure_log_shared_key = la_workspace_key
    table_name = os.environ["LogAnalyticsTable"]
    
        
    try:
        logging.info("trying post")
        post_data(
            azure_log_customer_id,
            azure_log_shared_key,
            json.dumps(json_data),
            table_name,
        )
        return func.HttpResponse("Data Posted to Log Analytics", status_code=201)

    except Exception as error:
        logging.error("Unable to send data to Azure Log")
        logging.error(error)




