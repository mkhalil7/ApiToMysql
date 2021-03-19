import  DatabaseHandler
import restApiHandler

#Attempting connection to API
if(restApiHandler.check_conenction_to_api()):
    print("Connection to API working ! ")
else:
    print("API down")

#checking our DB is app
DatabaseHandler.check_database_connection()



print(restApiHandler.get_pet_byId(2))

