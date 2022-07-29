
import requests
from pprint import pprint
from urllib import parse


def recommendation(title):
    pass
    # url로 인코드해주기
    titletourl = parse.urlencode({'query':f'{title}'},doseq = True)
    # & 붙여주기
    titletour2 = titletourl + '&'

    # 여기에 코드를 작성합니다.
    # urlencode랑 & 더한 결과값 가져오기
    response = requests.get(f'https://api.themoviedb.org/3/search/movie?api_key=61fdbed592643cc0f822b9040cad3a21&language=ko&{titletour2}page=1&include_adult=false')
    res = response.json()
    resultpg = res['results']
    # 응답 받은 결과 중 첫번째 영화의 id 값
    try:
        movie_id = resultpg[0]['id']
        # 해당 영화에 대한 추천 영화 목록 (Get Recommendations)을 가져옵니다.
        response2 = requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}/recommendations?api_key=61fdbed592643cc0f822b9040cad3a21&language=ko&page=1')
        res2 = response2.json()
        result = []
        if res2['results'] == []:
            return []
        else:
            for i in res2['results']:
                result.append(i['title'])
        return result
    except:
        return None
    
    

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화의 id를 기반으로 추천 영화 목록 구성
    추천 영화가 없을 경우 []를 반환
    영화 id 검색에 실패할 경우 None을 반환
    (주의) 추천 영화의 경우 아래 예시 출력과 차이가 있을 수 있음
    """
    pprint(recommendation('기생충'))
    # ['조커', '1917', '조조 래빗', ..생략.., '살인의 추억', '펄프 픽션']
    pprint(recommendation('그래비티'))
    # []
    pprint(recommendation('검색할 수 없는 영화'))
    # None"""
