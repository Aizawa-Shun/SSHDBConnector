import pymysql
import configparser
from sshtunnel import SSHTunnelForwarder
import pandas as pd
import datetime 
from data_exporter import export_data

# Load the configuration file
config = configparser.ConfigParser()
config.read('config.ini')

# SSH connection settings
ssh_host = config.get('SSH', 'ssh_host')
ssh_username = config.get('SSH', 'ssh_username')
ssh_key_path = config.get('SSH', 'ssh_key_path')
ssh_private_key_password = config.get('SSH', 'ssh_private_key_password')
ssh_password = config.get('SSH', 'ssh_password')
ssh_port = config.getint('SSH', 'ssh_port')

# Database connection settings
db_host = config.get('Database', 'db_host')
db_port = config.getint('Database', 'db_port')
db_user = config.get('Database', 'db_user')
db_password = config.get('Database', 'db_password')
db_name = config.get('Database', 'db_name')
charset = config.get('Database', 'charset')

# Table information
tables_info = {
    'EmployeeMaster': 'JoiningDate',
    'ExpenseReimbursement': 'RegistrationDate'
}

def connect_mysql(date_value):
    '''
    Connects to the MySQL database using an SSH tunnel and extracts and exports data from specific tables based on the specified date.
    This function establishes an SSH tunnel to connect to MySQL, executes queries filtered by the given date, and exports the results.
    
    Args:
        date_value (str): The date used as the basis for data extraction. The format is 'YYYY/MM'.
    
    Process:
        1. Connect to the MySQL server via an SSH tunnel.
        2. Execute SQL queries for each table to extract data from the specified date onwards.
        3. Export the extracted data to Excel and CSV files.
    
    Returns:
        None
    
    Exceptions:
        pymysql.Error: Raised if there is a problem during database connection or query execution.
    
    Notes:
        The database connection information is read from the config.ini file. The target tables are EmployeeMaster and ExpenseReimbursement.
    '''
    try:
        with SSHTunnelForwarder(
            (ssh_host, ssh_port),
            ssh_username=ssh_username,
            # ssh_password=ssh_password,
            ssh_pkey=ssh_key_path,
            ssh_private_key_password=ssh_private_key_password,
            remote_bind_address=(db_host, db_port),
        ) as server:
            conn = pymysql.connect(
                host='localhost',
                port=server.local_bind_port,
                user=db_user,
                password=db_password,
                database=db_name,
                charset=charset
            )
            print("Successfully connected to the database")

            # Calculate the start and end of the month
            start_date = datetime.datetime.strptime(date_value, '%Y/%m').replace(day=1)
            end_date = start_date + datetime.timedelta(days=31)
            end_date = end_date.replace(day=1) - datetime.timedelta(days=1)

            for table_name, date_column in tables_info.items():
                sql = f"SELECT * FROM `{table_name}` WHERE `{date_column}` >= %s AND `{date_column}` <= %s"
                df = pd.read_sql(sql, conn, params=[start_date.strftime('%Y/%m/%d'), end_date.strftime('%Y/%m/%d')])
                if not df.empty:
                    formatted_date = start_date.strftime('%Y年%m月')
                    export_data(df, table_name, formatted_date)
                else:
                    print(f"There is no data for {start_date.strftime('%Y/%m')} in the {table_name} table.")
    except pymysql.Error as e:
        print('Failed to connect to the database:', e)
    finally:
        if conn:
            print('Disconnecting from the database')
            conn.close()
