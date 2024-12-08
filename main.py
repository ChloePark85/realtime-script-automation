from app import create_app
from app.trend_analysis import fetch_trends
from app.script_generator import generate_script
from app.slack_api import upload_to_slack
import schedule
import threading
import time

# Flask 앱 생성
app = create_app()

# 작업 스케줄러 함수 정의
def run_scheduler():
    def task():
        keywords = fetch_trends()
        script = generate_script(keywords)
        upload_to_slack(script)
        print("스크립트가 생성되어 슬랙에 업로드되었습니다.")
    
    # 스케줄 작업 설정
    schedule.every(30).minutes.do(task)
    
    # 스케줄러 실행 루프
    while True:
        schedule.run_pending()
        time.sleep(1)

# Flask와 스케줄러를 동시에 실행
if __name__ == '__main__':
    # 스케줄러를 별도 스레드에서 실행
    scheduler_thread = threading.Thread(target=run_scheduler)
    scheduler_thread.daemon = True  # 메인 프로그램 종료 시 스레드도 종료
    scheduler_thread.start()
    
    # Flask 서버 실행
    app.run(debug=True, port=5000)