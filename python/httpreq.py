import json
from requests import Request, Session

url = "http://localhost:11435/api/chat"
#r = requests.get('http://localhost:11435/api/chat', stream=True)

s = Session()

req = Request('POST', url, data=data, headers=headers)
prepped = req.prepare()

# do something with prepped.body
prepped.body = '{"model": "llama3.2", "messages": [{"role": "system", "content": "$question"}, {"role": "user", "content": "$prompt"}]}'

# do something with prepped.headers
del prepped.headers['Content-Type']

r = s.send(prepped,
    stream=stream,
    verify=verify,
    proxies=proxies,
    cert=cert,
    timeout=timeout
)

for line in r.iter_lines():

    # filter out keep-alive new lines
    if line:
        decoded_line = line.decode('utf-8')
        print(json.loads(decoded_line))
