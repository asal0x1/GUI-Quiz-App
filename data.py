from pprint import pprint

import requests
q_types = {
    "amount": 10,
    "category": 31,
    "type": "boolean"
}
response = requests.get(url= "https://opentdb.com/api.php", params=q_types)
response.raise_for_status()
data = response.json()
question_data =(data["results"])

