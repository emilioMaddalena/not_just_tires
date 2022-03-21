import sys
sys.path.insert(0, '..')

import mysql.connector
from not_just_tires.secrets import MYSQL_USERNAME, MYSQL_PASSWORD, MYSQL_DB_NAME

MY_SQL_COMMAND = 'SHOW DATABASES'

my_db = mysql.connector.connect(
    host='localhost',
    user=MYSQL_USERNAME,
    passwd=MYSQL_PASSWORD
)

my_cursor = my_db.cursor()

my_cursor.execute(MY_SQL_COMMAND)

for msg in my_cursor: print(msg)