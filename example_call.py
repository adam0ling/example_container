import requests
import json

request = {
    "OcrValue": ["#P.MOLDE 100% INT", "6 HUEVOS - L -"]
    }

response = requests.post("http://0.0.0.0:80/cleanup", json=request)

print(response.json())

prettyJson = json.dumps(response.json(), indent=4)
exampleJson = open('example.json', 'w', encoding='utf-8-sig')
exampleJson.write(prettyJson)
exampleJson.close()