import json

handle = open("temp.json", "r")
content = handle.read()

d = json.loads(content)
print(d['users'])
