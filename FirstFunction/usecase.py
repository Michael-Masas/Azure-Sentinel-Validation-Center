## this Class is defualt JSON Data for Log Analytics API if no specified JSON was mentioned as parameter in Post Data function.
class Default :
    data = {
        "message": "no relevant data or json data was chosen"
    }

class Conditional:
    data = {
"TimeGenerated": "8/4/2021, 3:58:01.000 PM",
"Browser": "Chrome 92.0.4515",
"StatusCode": "50126",
"ConditionalAccessStatus": "Failure",
"ConditionalAccessPol0Name": "0",
"IPAddress": "131.107.159.34",
"Location":  "Redmond, Washington",
"UserPrincipalName": "noam.pilo@cyberproof.com",
"Action": "Denied",
"AppDisplayName": "Microsoft Teams",
"OS": "Windows 10",
"detailsMessage": "User did not respond to mobile app notification"
}

class UnAuthAADPS:
    data = {
"AppId ": "1b730954-1685-4b74-9bfd-dac224a7b894",
"AppDisplayName": "Azure Active Directory PowerShell",
"TokenIssuerType ": "AzureAD",
"ResourceIdentity": "9cdead84-a844-4324-93f2-b2e6bb768d07",
"Status": {"errorCode":"0"},
"IPAddress": "131.107.159.34",
"UserAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36",
"ResourceDisplayName": "Windows Virtual Desktop",
"UserDisplayName": "Noam Pilo",
"UserId": "c62e092f-5e87-48d8-ac49-cdeb311b4703",
"UserPrincipalName": "noam.pilo@cyberproof.com",
"Type": "AuditLogs"
}

class PScmdlets:
    data = {
"EventID": "4688",
"SubjectUserName": "ADMNoam",
"SubjectDomainName": "Win81",
"Computer": "CP-GMFZJR2",
"Process": "C:\WINDOWS\system32\powershell.exe",
"CommandLine": "Set-Killdate 811123200"
}

class MultiRDP:
    data = {
"EventID": "4624",
"LogongType": "10",
"Computer": "CP-GMFZJR2",
"ProcessName": "C:\Windows\System32\svchost.exe",
"Account": "ADMNoam",
"IpAddress":"131.107.159.34",
"AccountType": "Administrator",
"Activity": "Logon",
"LogonTypeName": "RDP"
}

class MFAdisabled2:
    data = {
"EventName": "DeactivateMFADevice",
"requestParameters": {
        "userName": "AWS ROOT USER",
        "InstanceProfileName": "Noam Pilo"
},
"EventSource": "portal.azure.com",
"SourceIpAddress": "131.107.159.34"
}

class MFAdisabled1:
    data = {
"OperationName": "Disable Strong Authentication",
"InitiatedBy.user": {
"ipAddress": "131.107.159.34",
"userPrincipalName": "ADMNYeho",
"displayName": "Yehonatan"
},
"Targetprop": {
"userPrincipalName": "NoamPilo"
},
"CorrelationId": "082312f1-9265-4707-8ee2-e845407b870b",
"Category": "UserManagement",
"SourceSystem": "Azure AD",
"AADTenantId": "10fb7203-c2cb-4477-8faf-a8607d775678",
"Type": "AuditLogs"
}

