import json

with open('controllerData.json','r') as f:
    data = json.load(f)


print(data)