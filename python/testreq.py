import json
import re
from requests import Request, Session

def read_file(file_path: str):
    """
    Read some text from a text file.
    """
    with open(file_path, "r") as f:
        file_data = f.read()
        original_string = file_data.replace("\n", " ")
        modified_string = re.sub(r'"', "'", original_string)
        return modified_string

prompt_path = "./prompt.txt"
prompt_data = read_file(prompt_path)
print({prompt_data})
question_path = "/home/ec2-user/metadata/data/prompts/medical_progress_notes_prompt.txt"
question_data = read_file(question_path)
print(question_data)
url1 = "http://localhost:53795/api/test/Service"
data = '{"model": "llama3.2", "messages": [{"role": "system", "content": "$question"}, {"role": "user", "content": "$prompt"}]}'
data1 = data.replace("$question",question_data)
data2 = data1.replace("$prompt",prompt_data)
print(data2)
s = Session()
url2 = "http://localhost:11435/api/chat"
req = Request('POST', url2, data=data2,)
#prepped = req.prepare()
prepped = s.prepare_request(req)

# Merge environment settings into session
settings = s.merge_environment_settings(prepped.url, {}, None, None, None)

# do something with prepped.body
# prepped.body = '{"model": "llama3.2", "messages": [{"role": "system", "content": "$question"}, {"role": "user", "content": "$prompt"}]}'
prepped.body = data2

# do something with prepped.headers
#del prepped.headers['Content-Type']
#r = s.send(prepped, **settings)
timeout = 300
resp = s.send(prepped,
    stream=False,
#    verify=verify,
#    proxies=proxies,
#    cert=cert,
    timeout=timeout
)

answer = []

#for line in r.iter_lines():
for line in resp.iter_lines():

    # filter out keep-alive new lines
    if line:
        decoded_line = line.decode('utf-8')
        y = (json.loads(decoded_line))
        message = y["message"]
        content = message["content"]
        answer.append(content)

print(str(answer))

