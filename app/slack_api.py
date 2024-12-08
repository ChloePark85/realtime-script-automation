import requests

SLACK_WEBHOOK_URL = "https://hooks.slack.com/services/your/webhook/url"

def upload_to_slack(script):
    payload = {
        "text": script,
        "attachments": [
            {
                "text": "확인 후 '사운드 변환' 버튼을 클릭하세요.",
                "callback_id": "convert_to_audio",
                "actions": [
                    {
                        "name": "convert",
                        "text": "사운드 변환",
                        "type": "button",
                        "value": "convert"
                    }
                ]
            }
        ]
    }
    requests.post(SLACK_WEBHOOK_URL, json=payload)