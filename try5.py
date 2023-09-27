import requests, sys, json

try:
    response = requests.get("https://cs50.harvard.edu/python/2022/psets/4/")
except:
    sys.exit("Couldn't get the response for the request")
else:
    print(json.dumps(response.json()))