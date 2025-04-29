import json
from requests import Request, Session

url = "http://localhost:11435/api/chat"
data = '{"model": "llama3.2", "messages": [{"role": "system", "content": "$question"}, {"role": "user", "content": "$prompt"}]}'

s = Session()

req = Request('POST', url, data=data,)
#prepped = req.prepare()
prepped = s.prepare_request(req)

# Merge environment settings into session
settings = s.merge_environment_settings(prepped.url, {}, None, None, None)

# do something with prepped.body
prepped.body = '{"model": "llama3.2", "messages": [{"role": "system", "content": "$question"}, {"role": "user", "content": "$prompt"}]}'

# do something with prepped.headers
#del prepped.headers['Content-Type']
r = s.send(prepped, **settings)

for line in r.iter_lines():

    # filter out keep-alive new lines
    if line:
        decoded_line = line.decode('utf-8')
        print(json.loads(decoded_line))
