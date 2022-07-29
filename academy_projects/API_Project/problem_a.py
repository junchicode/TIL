import requests
import json
from pprint import pprint

key = '61fdbed592643cc0f822b9040cad3a21'

def popular_count():
    pass
    url = 'https://api.themoviedb.org/3/movie/popular?api_key=61fdbed592643cc0f822b9040cad3a21&language=ko&page=1'
    response = requests.get(url)
    res = response.json()
    resultpg = res['results']
    return len(resultpg)
    # 여기에 코드를 작성합니다.  
    
        

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20