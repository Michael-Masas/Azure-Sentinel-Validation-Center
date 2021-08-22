# Introduction 
This Is a Use Case Testing Script Platform Via Azure Function Apps. \
Basically This App Pushes Dummy Information to Azure Log Analytics in order to check rules and alerts configured on azure Sentinel. \


# Getting Started
Folder Structure 
Direcotory : FirstFunction :
__init__.py -- main file for Function App \
function.json -- configuration for function app \
usecase.py -- file for Conditional Access Use Case Data - Classes File
defualt.py -- file if no use case file was configured on Parameter in Function APP \


# Use and Test
Variables :
on main (FirstFunction): 

To Use the Function -> Deploy The Function App to Azure and use the name of the Use case in get_file_by_name Function \
azure_log_customer_id = -> Goes to Veriable -> la_workspace_id = os.environ["WorkspaceID"] -- from Function App Application Settings \
azure_log_shared_key = -> Goes to Veriable -> la_workspace_key = os.environ["WorkspaceKey"] -- from Function App Application Settings \
table_name = 'os.environ["LogAnalyticsTable"] -- > Azure LA Custom Table Name - From Function App Application Settings






