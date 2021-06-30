import mysql.connector

# DB params
host = "localhost"
user = "user"
password = "123456"
database = "petStore"
db = ""

# Establishing connection to DB
try:
    db = mysql.connector.connect(host=host, user=user, password=password, database=database)
except:
    print("termaninating the script Connection to DB cannont be made")
    exit(0)

db.cursor()


# Checking the conenction to the DB
def check_database_connection():
    if (db == ""):
        print("Cannot connect to DB ")
        return True

    else:
        print("Database conection is ready ")
        return False
