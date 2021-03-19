import requests
import  mysql.connector
import string
import base64

def print_hi(name1, name2, name3):
    print(name1,name2,name3)


def load_data():
    #connect to the petstore API and send request to get pet
    url = "https://petstore.swagger.io/v2/pet/1"
    path = "/pet/"

    data_array = []

    #go throuh the API
    for id in range(0,10) :

        params= {'id': id}
        print (params)
        r = requests.get(url=url, data=params)
        response_json = r.json()
        print (response_json)
        data_array.append(response_json)

    return data_array





if __name__ == '__main__':

    data = load_data()
    print (data)

