from hashlib import new
import json
from pprint import pprint



def movie_info(movie, genres):
    pass 
    # 여기에 코드를 작성합니다.  
    new_data = {
        'id': movie.get('id'),
        'title': movie.get('title'),
        'poster_path': movie.get('poster_path'),
        'vote_average': movie.get('vote_average'),
        'overview': movie.get('overview'), 
        'genre_ids': movie.get('genre_ids')
    }
    new_dictforgen ={}
    for i in genres:
        k = i.get('id')
        v = i.get('name')
        new_dictforgen.update({k:v})
        
    new_id = []
    for i in new_data['genre_ids']:
        new_id.append(new_dictforgen.get(i))
        

    new_data['genre_ids'] = new_id
    
    return new_data        
        
            
        

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='utf-8')
    movie = json.load(movie_json)

    genres_json = open('data/genres.json', encoding='utf-8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie, genres_list))
