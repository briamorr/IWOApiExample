import json
import requests

from intersight_auth import IntersightAuth

def getActions():
    RESPONSE = requests.request(
        method="GET",
        url="https://intersight.com/wo/api/v3/markets/Market/actions?ascending=false&disable_hateoas=true&limit=1000&order_by=severity",
        auth=AUTH
    )

    record = RESPONSE.json()

    for group in record:
        if group["target"]["displayName"] == 'te-useast-aws':
            print(group["uuid"],group["target"]["className"],group["target"]["displayName"],group["details"],group["actionID"],group["actionState"])

#Configure Intersight API token       
AUTH = IntersightAuth(
    secret_key_filename='SecretKey.txt',
    api_key_id='xxxx/yyyy/zzzz'
    )

getActions()
