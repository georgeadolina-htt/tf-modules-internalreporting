import urllib3
import json
http = urllib3.PoolManager()


def lambda_handler(event, context):
    url = "https://hooks.slack.com/services/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"
    msg = {
        "channel": "deployment-internal-reporting",
        "username": "WEBHOOK_USERNAME",
        "text": event['Records'][0]['Sns']['Message'],
        "icon_emoji": ""
    }

    encoded_msg = json.dumps(msg).encode('utf-8')
    resp = http.request('POST', url, body=encoded_msg)
    print({
        "message": event['Records'][0]['Sns']['Message'],
        "status_code": resp.status,
        "response": resp.data
    })
