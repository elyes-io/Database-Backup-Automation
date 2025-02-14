from datetime import datetime
import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

database_user = os.getenv("DATABASE_USER")
database_password = os.getenv("DATABASE_PASSWORD")
database_name = os.getenv("DATABASE_NAME")
port = os.getenv("PORT")
host = os.getenv("HOST")

current_day = datetime.now()
date = current_day.strftime("%Y-%m-%d_%H-%M-%S")
backup_filename = f"{database_name}_backup_{date}.sql"

conn = mysql.connector.connect(
    host=host,
    user=database_user,
    password=database_password,
    database=database_name,
    port=port
)

cursor = conn.cursor()
cursor.execute("SHOW TABLES")
tables = cursor.fetchall()

with open(backup_filename, "w") as f:
    for table in tables:
        table_name = table[0]
        cursor.execute(f"SHOW CREATE TABLE {table_name}")
        schema = cursor.fetchone()[1]
        f.write(f"{schema};\n\n")

        cursor.execute(f"SELECT * FROM {table_name}")
        rows = cursor.fetchall()
        for row in rows:
            values = ', '.join([f"'{str(value).replace("'", "''")}'" if value is not None else 'NULL' for value in row])
            f.write(f"INSERT INTO {table_name} VALUES ({values});\n")

conn.close()

print(f"Backup successful: {backup_filename}")
