import json, datetime, requests
import pandas as pd

def get_elasticsearch_logs():
    elasticsearch_url = 'http://localhost:9200'
    response = requests.post(url=f'{elasticsearch_url}/fluentd-2019/_search', 
                            data=json.dumps({"query": {
                                                "bool" : {
                                                    "filter" : {
                                                        "term" : { "@log_name" : "app.prediction" }
                                                    }
                                                }
                                            }}), 
                            headers= {'Content-Type': 'application/json'})

    return response.json()

def save_json_as_csv(json_):
    logs = json_['hits']['hits']
    data = [log['_source'] for log in logs]
    df = pd.DataFrame(data)
    now_timestamp = datetime.datetime.today().strftime('%Y%m%d%H%m')
    
    df.to_csv(f'./data/{now_timestamp}-dataset.csv')
    

if __name__ == '__main__':
    logs_json = get_elasticsearch_logs()
    save_json_as_csv(logs_json)