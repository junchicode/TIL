import json

def movie_info(movie):
    pass 
    # 여기에 코드를 작성합니다.    
    new_data = {
        movie["revenue"]: movie["title"]    
    }
    return new_data

def max_revenue(movies):
    pass 
    # 여기에 코드를 작성합니다.
    mvlist = []
    ttlist = []
    price = []
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
        
    res = max(eachmoviedict)
    return eachmoviedict[res]
                
        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)
    
    print(max_revenue(movies_list))
