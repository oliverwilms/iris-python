import json
import requests

url = "http://localhost:11435/api/chat"
r = requests.get('http://localhost:11435/api/chat', stream=True)

for line in r.iter_lines():

    # filter out keep-alive new lines
    if line:
        decoded_line = line.decode('utf-8')
        print(json.loads(decoded_line))
