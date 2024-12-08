from pytrends.request import TrendReq
import random

def fetch_trends():
    """
    Google Trends에서 상위 5개 키워드를 가져오고, 그 중 가장 트렌드인 첫 번째 키워드를 반환합니다.
    """
    try:
        pytrends = TrendReq()
        trending_searches = pytrends.trending_searches(pn="south_korea")
        top_5_keywords = trending_searches[0:5].values.flatten().tolist()
        main_keyword = top_5_keywords[0]  # 가장 트렌드인 키워드
        return top_5_keywords, main_keyword
    except Exception as e:
        print(f"트렌드 가져오기 실패: {str(e)}")
        backup_keywords = [
            '막장', '배신', '복수', '재벌', '사랑'
        ]
        return backup_keywords, backup_keywords[0]