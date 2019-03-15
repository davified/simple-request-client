import time, json, random
import requests

def randomize(num):
    return round(num * random.uniform(0, 10), 2)



for i in range(20):
    base_url = 'http://localhost:8080'
    # base_url = 'http://35.247.170.228/'
    response = requests.post(url=f'{base_url}/predict', 
                             data=json.dumps({ 
                                "AGE": randomize(65.2),
                                "B": randomize(396.9),
                                "CHAS": randomize(1),
                                "CRIM": randomize(1),
                                "DIS": randomize(4.09),
                                "INDUS": randomize(2.31),
                                "LSTAT": randomize(4.98),
                                "NOX": randomize(0.538),
                                "PTRATIO": randomize(15.3),
                                "RAD": randomize(1.0),
                                "RM": randomize(200),
                                "TAX": randomize(296),
                                "ZN": randomize(18)
                            }), 
                            headers= {'Content-Type': 'application/json'})
    time.sleep(1)
    print(response.text)