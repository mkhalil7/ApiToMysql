import requests

url = "https://petstore.swagger.io/v2/pet/1"
path = "/pet/"


def load_data():
    #connect to the petstore API and send request to get pet
    data_array = []
    #go throuh the API
    for id in range(0,10) :
        params= {'id': id}
        print (params)
        r = requests.get(url=url, data=params)
        response_json = r.json()
        print(response_json)
        data_array.append(response_json)
    return data_array