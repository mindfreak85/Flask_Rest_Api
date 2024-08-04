import requests

BASE = "http://127.0.0.1:5000"

data = [{"likes":10, "name":"Video0", "views": 100000}, 
        {"likes":2000, "name":"Video1", "views": 100000}, 
        {"likes":23010, "name":"Video2", "views": 100000}]


for i in range(len(data)):
    response = requests.put(BASE + "/video/" + str(i), json=data[i])
    print(response.json())


response = requests.get(BASE + "/video/6")
print(response.json())



