import requests
import os
from dotenv import load_dotenv
import time

# Slack Webhook URL
SLACK_WEBHOOK_URL = os.getenv("SLACK_WEBHOOK_URL")

def upload_to_slack(all_keywords, main_keyword, script):
    """
    트렌드 키워드들과 오디오드라마 스크립트를 Slack에 업로드합니다.
    """
    text = (
        f"🎯 *실시간 트렌드 키워드 TOP 5*\n"
        f"```{', '.join(all_keywords)}```\n\n"
        f"🌟 *선정된 메인 키워드*\n"
        f"```{main_keyword}```\n\n"
        f"📝 *오디오드라마 스크립트*\n"
        f"```{script}```\n\n"
        f"_Generated at: {time.strftime('%Y-%m-%d %H:%M:%S')}_"
    )
    
    payload = {
        "blocks": [
            {
                "type": "header",
                "text": {
                    "type": "plain_text",
                    "text": "🎬 새로운 오디오드라마 스크립트가 생성되었습니다!"
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f"🎯 *트렌드 키워드 TOP 5*\n{', '.join([f'`{kw}`' for kw in all_keywords])}"
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f"🌟 *선정된 메인 키워드*\n`{main_keyword}`"
                }
            },
            {
                "type": "divider"
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f"📝 *오디오드라마 스크립트*\n{script}"
                }
            }
        ]
    }
    
    response = requests.post(SLACK_WEBHOOK_URL, json=payload)
    if response.status_code != 200:
        print(f"슬랙 업로드 실패: {response.text}")
        return False
    return True
