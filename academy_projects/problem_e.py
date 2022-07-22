import json

def movie_info(movie):
    pass 
    # 여기에 코드를 작성합니다.
    movie["release_date"] = movie['release_date'][5:7]    
    new_data = {
        movie["title"]: movie["release_date"],    
    }
    return new_data

def dec_movies(movies):
    pass 
    # 여기에 코드를 작성합니다.
    mvlist = []
    ttlist = []
    for i in movies_list:
        mvlist.append(i['id'])
        ttlist.append(i['title'])
    
    eachmoviedict = {}
    for i in mvlist:
        if __name__ == '__main__':
            eachmovie = open(f'data/movies/{i}.json', encoding = 'utf-8')
            eachmovieopen = json.load(eachmovie)
            eachres = movie_info(eachmovieopen)
            eachmoviedict.update(eachres)
    
    reslist = []
    for k,v in eachmoviedict.items():
        if v == '12':
            reslist.append(k)
    
    return reslist
    

if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)
    
    print(dec_movies(movies_list))
