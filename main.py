import  DatabaseHandler
import restApiHandler


print("Welcome to our test script for API  \n")



#Attempting connection to API
if(restApiHandler.check_conenction_to_api()):
    print("Connection to API working ! \n")
else:
    print("API down \n")

#checking our DB is app
DatabaseHandler.check_database_connection()



#print(restApiHandler.get_pet_byId(2))

