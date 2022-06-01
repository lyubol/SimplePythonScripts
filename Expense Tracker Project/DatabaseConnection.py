# Setup connection to Azure SQL Database

import pyodbc

# connection details
server = ""
database = ""
username = ""
password = ""
driver = "{ODBC Driver 17 for SQL Server}"

conn = pyodbc.connect( 
    "Driver = {SQL Server};"
    "Server = server_name;"
    "Database = database_name;"
    "Trusted_Connection = yes"
)
