from app import create_app
from app.trend_analysis import fetch_trends
from app.script_generator import generate_script
from app.slack_api import upload_to_slack
import schedule
import threading
import time

# Flask 앱 생성
app = create_app()

def execute_task():
    """단일 작업 실행 함수"""
    try:
        # 트렌드 키워드 가져오기
        all_keywords, main_keyword = fetch_trends()
        print(f"분석된 키워드: {all_keywords}")
        print(f"선정된 메인 키워드: {main_keyword}")

        # 스크립트 생성
        script = generate_script(main_keyword)
        print(f"스크립트 생성 완료: {len(script)} 자")

        # Slack에 업로드
        success = upload_to_slack(all_keywords, main_keyword, script)
        if success:
            print("슬랙 업로드 완료")
        else:
            print("슬랙 업로드 실패")
            
    except Exception as e:
        print(f"작업 실행 중 오류 발생: {str(e)}")

# 작업 스케줄러 함수 정의
def run_scheduler():
    # 시작하자마자 한 번 실행
    execute_task()
    
    # 30분마다 실행되도록 스케줄 설정
    schedule.every(30).minutes.do(execute_task)
    
    # 스케줄러 실행 루프
    while True:
        schedule.run_pending()
        time.sleep(1)

# Flask와 스케줄러를 동시에 실행
if __name__ == '__main__':
    try:
        # 스케줄러를 별도 스레드에서 실행
        scheduler_thread = threading.Thread(target=run_scheduler)
        scheduler_thread.daemon = True  # 메인 프로그램 종료 시 스레드도 종료
        scheduler_thread.start()
        
        # Flask 서버 실행
        app.run(debug=False, port=5000)  # debug 모드를 False로 설정
    except KeyboardInterrupt:
        print("프로그램을 종료합니다...")
    except Exception as e:
        print(f"프로그램 실행 중 오류 발생: {str(e)}")