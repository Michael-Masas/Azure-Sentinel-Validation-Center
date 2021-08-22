# Introduction 
This Is a Use Case Testing Script Platform Via Azure Function Apps. \
Basically This App Pushes Dummy Information to Azure Log Analytics in order to check rules and alerts configured on azure Sentinel. \
The Alerts and Triggers needs to Based on the Function's APP Log Anlytics Table Configured within the Application Settings of the Function App. 
A Storage Account is required for this Function APP. 

# Getting Started
Function Folder Structure
Direcotory : FirstFunction :
__init__.py -- main file for Function App \
function.json -- configuration for function app \
usecase.py -- file for Use Case Data - Classes File - Import the Classes and Add them to The get_file_by_name Class \
defualt.py -- file if no use case file was configured on Parameter in Function APP \

# Deploy Application
Deploy The Azure Function APP - As Normally you would deploy an azure Function APP 
https://docs.microsoft.com/en-us/azure/azure-functions/create-first-function-vs-code-python \
Push the "FirstFunction" Directory as an HTTP Trigger Function \
Deploy to Azure - This Will Create a URL that can Be used to Push the Data To Log Analytics. 

# Application Settings
The Application Needs some Settings To Be Configured After Deployment \
After The Deployment of the Azure Function App -> Go To -> Settings -> Configuration and Input the Follwing Application Settings : \
LogAnalyticsTable - The Value of this Setting will be name of the Custom Table within Log Anlytics Workspace which Azure Sentinel Uses \
WorkspaceID - The Value of this Setting will be the WorkSpace ID for Log Analytics Workspace \
WorkspaceKey - The Value of this Setting will be the WorkSpace Key for Log Analytics Workspace \
AzureWebJobsAzureStorageQueuesConnectionString - Storage Account Connection String for Storing the Functions Files \
AzureWebJobsStorage - Storage Account Connection String for Function's Deployment  \
WEBSITE_CONTENTAZUREFILECONNECTIONSTRING - Automated Storage Account Connection String \

All Three Connection String Can be to the Same Storage Account.


# Use and Test
Variables :
on main (FirstFunction): 

To Use the Function -> Deploy The Function App to Azure and use the name of the Use case in get_file_by_name Function \
azure_log_customer_id = -> Goes to Veriable -> la_workspace_id = os.environ["WorkspaceID"] -- from Function App Application Settings \
azure_log_shared_key = -> Goes to Veriable -> la_workspace_key = os.environ["WorkspaceKey"] -- from Function App Application Settings \
table_name = 'os.environ["LogAnalyticsTable"] -- > Azure LA Custom Table Name - From Function App Application Settings

For e.g : 
Run this URL to Trigger the Conditional Access Use case - It Will Push Log Analytics Table According to the 'LogAnalyticsTable' Application Settings In The Function APP

https://v-center.azurewebsites.net/api/firstfunction?name=multirdp


