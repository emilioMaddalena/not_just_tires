import sys
sys.path.insert(0, '..')

import mysql.connector
from not_just_tires.secrets import DB_ENDPOINT, DB_PORT, DB_USER, DB_PASSWORD
from sql_script import SQL_SCRIPT

my_db = mysql.connector.connect(
    host=DB_ENDPOINT,
    port=DB_PORT,
    user=DB_USER,
    passwd=DB_PASSWORD
)

my_cursor = my_db.cursor()

for sql_command in SQL_SCRIPT:
    print('\n~ Command:')
    print(sql_command)
    my_cursor.execute(sql_command)
    
    print('~ Output:')
    for msg in my_cursor: print(msg)