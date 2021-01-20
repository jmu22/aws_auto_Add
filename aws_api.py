import requests
import os

from requests.auth import HTTPBasicAuth


inputfile = open('aws_accounts.txt')
headers={'Content-type':'application/json', 'Accept':'application/json'}

for line in inputfile:
    line = line.strip('\n')
    myobj = {
        "account_id": line,
        "access_role_name": "svc-operations-snow-crossaccount",
        "accessor_id": "142855751540"
    }
    response = requests.post("https://asuriondev.service-now.com/api/asrp/aws_endpoint/snowdiscovery", json = myobj, headers = headers,  auth=HTTPBasicAuth(os.environ.get('asurion_user'),os.environ.get('asurion_pass')))
    if (response.status_code != 200):
        print("Failed to discover datacenters for account " + line + " The error is " + str(response.status_code))
    else:
        print("Successfully added AWS Account " + line)
print("Job has finished")








