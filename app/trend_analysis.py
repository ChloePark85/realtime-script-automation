from pytrends.request import TrendReq

def fetch_trends():
    pytrends = TrendReq()
    trending_searches = pytrends.trending_searches(pn="united_states")
    return trending_searches[0:5].values.flatten().tolist()