# app 모듈 가져오기
from app.trend_analysis import fetch_trends

def test_trend_analysis():
    keywords = fetch_trends()
    assert len(keywords) > 0, "트렌드 키워드가 비어 있습니다!"
    print(f"트렌드 키워드: {keywords}")

if __name__ == "__main__":
    test_trend_analysis()