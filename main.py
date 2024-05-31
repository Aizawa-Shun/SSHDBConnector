import mysql_tunnel_connector 
import utils 

def main():
    '''
    Select a specific date using a user interface,
    and connect to a MySQL database via an SSH tunnel with the selected date.
    
    This function executes the following steps:
    1. Date selection: The user selects a date through the GUI.
    2. Database connection: Attempts to connect to the MySQL database using the selected date as a parameter.
    3. Outputs the result to Excel/CSV
    
    Returns:
        None
    '''
    # Select the registration date using the GUI
    date = utils.display()
    # Establish an SSH tunnel and connect to MySQL
    mysql_tunnel_connector.connect_mysql(date)

if __name__ == '__main__':
    main()
