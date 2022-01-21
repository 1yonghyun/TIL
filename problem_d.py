import json


def max_revenue(movies):
    pass 
    # 여기에 코드를 작성합니다.  
    
    rev = 0
    result = 0
    
    for movie in movies:
        

        id = movie.get('id')
        title = movie.get('title')    
        if __name__ == '__main__':
            movies_json = open(f'data/movies/{id}.json', encoding='UTF8')
            movies_info = json.load(movies_json)
            m = movies_info.get("revenue") 

        if m > rev:
            rev = m
            result = title
        
    return result
    
#아래의 코드는 수정하지 않습니다.

if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)
    
    print(max_revenue(movies_list))