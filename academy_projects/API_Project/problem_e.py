from urllib import parse
import requests
from pprint import pprint
from operator import itemgetter


def credits(title):
    pass 
    # 여기에 코드를 작성합니다.  
    # url로 인코드해주기
    titletourl = parse.urlencode({'query':f'{title}'},doseq = True)
    # & 붙여주기
    titletour2 = titletourl + '&'

    # 여기에 코드를 작성합니다.
    # urlencode랑 & 더한 결과값 가져오기
    response = requests.get(f'https://api.themoviedb.org/3/search/movie?api_key=61fdbed592643cc0f822b9040cad3a21&language=ko&{titletour2}page=1&include_adult=false')
    res = response.json()
    if res['total_results'] == 0:
        return None
    else:
        resultpg = res['results']
        # 응답 받은 결과 중 첫번째 영화의 id 값
    
        movie_id = resultpg[0]['id']
        # 해당 영화에 대한 (Get Credits)을 가져옵니다.
        response2 = requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key=61fdbed592643cc0f822b9040cad3a21&language=ko')
        res2 = response2.json()
        cast = res2['cast']
        castidunder10 = []
        castfinallist = []
        for i in cast:
            if i['cast_id'] <= 10:
                castidunder10.append(i)
            else:
                pass
        for j in castidunder10:
            castfinallist.append(j['name'])
            
        crew = res2['crew']
        crews = []
        
        for c in crew:
            if c['department'] == 'Directing':
                crews.append(c['name'])
            else:
                pass
        
        result = {'cast': castfinallist, 'directing': crews}
        
        return result
            
        


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화 id를 통해 영화 상세정보를 검색하여 주연배우 목록(cast)과 스태프(crew) 중 연출진 목록을 반환
    영화 id 검색에 실패할 경우 None을 반환
    """
    pprint(credits('기생충'))
    # {'cast': ['Song Kang-ho', 'Lee Sun-kyun', ..., 'Jang Hye-jin'], 'crew': ['Bong Joon-ho', 'Park Hyun-cheol', ..., 'Yoon Young-woo']}
    pprint(credits('검색할 수 없는 영화'))
    # None
