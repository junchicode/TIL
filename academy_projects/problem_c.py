import json
from pprint import pprint
from turtle import st


def movie_info(movies, genres):
    pass 
    # 여기에 코드를 작성합니다.  
    pb_c_res = []
    for i in movies:
        new_data = {
        'id': i.get('id'),
        'title': i.get('title'),
        'poster_path': i.get('poster_path'),
        'vote_average': i.get('vote_average'),
        'overview': i.get('overview'), 
        'genre_ids': i.get('genre_ids')}
    
        new_dictforgen ={}
        for i in genres:
            k = i.get('id')
            v = i.get('name')
            new_dictforgen.update({k:v})
            
        new_id = []
        for i in new_data['genre_ids']:
            new_id.append(new_dictforgen.get(i))
            
        new_data['genre_ids'] = new_id
        
        pb_c_res.append(new_data)

    return pb_c_res
    
    
            
        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='utf-8')
    genres_list = json.load(genres_json)
    pprint(movie_info(movies_list, genres_list))
    





