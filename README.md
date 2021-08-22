# Introduction 
This Is a Use Case Testing Script Platform Via Azure Function Apps. \
Basically This App Pushes Dummy Information to Azure Log Analytics in order to check rules and alerts configured on azure Sentinel. \


# Getting Started
Folder Structure 
Direcotory : FirstFunction :
__init__.py -- main file for Function App \
function.json -- configuration for function app \
conditional.py -- file for Conditional Access Use Case Data \
defualt.py -- file if no use case file was configured on Parameter in Function APP \


# Use and Test
Variables :
on main function : 

parameter_from_azure = os.environ["UseCase"] \ 
azure_log_customer_id = 'INSERT AZURE LA WORKSPACE ID' \ 
azure_log_shared_key =  'INSERT AZURE LA WORKSPACE KEY' \ 
table_name = 'DummyData' -- > Azure LA Custom Table Name \



