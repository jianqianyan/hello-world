import requests
import json
import time

url='https://oapi.dingtalk.com/robot/send?access_token=1dc6bb15a0896102b561283cd7cbf76871f32a7721280baf6de4e168e609b2b8'

obj={
    "msgtype": "text",
    "text": {
        "content": 'B,.....'
    }
}

requests.post(url,
    headers={'Content-Type': 'application/json'},
    data=json.dumps(obj)
)
