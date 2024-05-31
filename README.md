
# MySQL Data Export Tool
This project provides a tool to connect to a MySQL database through an SSH tunnel, extract data based on user-selected dates, and export the data to both Excel and CSV formats.

## Features

- Date Selection GUI: A user-friendly interface to select a specific date.
- SSH Tunnel Connection: Securely connect to a MySQL database using SSH tunneling.
- Data Extraction: Extract data from specified tables based on the selected date.
- Data Export: Export the extracted data to Excel and CSV files with automatically adjusted column widths in Excel.


## Installation

1. Clone the repository:

```bash
  git clone https://github.com/Aizawa-Shun/SSHDBConnector.git
```

2. Install required packages:

```bash
  pip install -r requirements.txt
```

3. Configuration:
```ini
[SSH]
ssh_host = your_ssh_host
ssh_username = your_ssh_username
ssh_key_path = your_ssh_key_path
ssh_private_key_password = your_ssh_private_key_password
ssh_password = your_ssh_password
ssh_port = your_ssh_port

[Database]
db_host = your_db_host
db_port = your_db_port
db_user = your_db_user
db_password = your_db_password
db_name = your_db_name
charset = your_db_charset

```
## Usage/Examples

1. Start the GUI for Date Selection:

- The display function in utils.py launches the GUI for date selection.
- The selected date is then used to filter data from the database.
```Python
import utils
date = utils.display()

```

2. Connect to MySQL and Export Data:

- The connect_mysql function in mysql_tunnel_connector.py connects to the MySQL database through an SSH tunnel and extracts data based on the selected date.
```Python
import mysql_tunnel_connector
mysql_tunnel_connector.connect_mysql(date)

```
## Project Structure
- config.ini: Configuration file for SSH and database connection settings.
- data_exporter.py: Contains the export_data function to export data to Excel and CSV files.
- mysql_tunnel_connector.py: Establishes an SSH tunnel and connects to the MySQL database to extract and export data.
- utils.py: Contains the display function to show the date selection GUI.
- gui.py: Implements the GUI class to create the date selection interface.
## Functions

### utils.py

#### display()

Displays the date selection screen using the GUI and returns the date selected by the user.
Returns:

- str: The date selected by the user as a string in the format YYYY/MM/DD.

### mysql_tunnel_connector.py

#### connect_mysql(date_value)
Connects to the MySQL database using an SSH tunnel and extracts and exports data from specific tables based on the specified date.
Args:

- date_value (str): The date used as the basis for data extraction. The format is YYYY/MM.

### data_exporter.py
#### export_data(df, table_name, formatted_date)
Exports the given DataFrame to an Excel file and a CSV file.
Args:

- df (pandas.DataFrame): DataFrame containing the data to be exported.
- table_name (str): The name of the table for the output data. Used as the sheet name in Excel and the filename for the CSV file.
- formatted_date (str): Date string used in the output filenames.

#### adjust_column_width_from_df(worksheet)
Adjusts the column width of the specified Excel worksheet based on the maximum length of the data contained in the cells of each column.
Args:

- worksheet (openpyxl.worksheet.worksheet.Worksheet): The worksheet object whose column width needs to be adjusted.
## License

This project is licensed under the [MIT License](https://github.com/Aizawa-Shun/SSHDBConnector.git/LICENSE)
