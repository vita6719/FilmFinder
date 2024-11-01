import requests
import json

# Ваш ключ API от TMDb
api_key = 'ваш_ключ_API'

def search_movie(movie_title):
    url = f'https://api.themoviedb.org/3/search/movie?api_key={api_key}&query={movie_title}'
    
    response = requests.get(url)
    data = response.json()
    
    if len(data['results']) == 0:
        print("Фильм не найден.")
        return
    
    first_result = data['results'][0]
    
    movie_id = first_result['id']
    title = first_result['title']
    release_date = first_result['release_date']
    overview = first_result['overview']
    vote_average = first_result['vote_average']
    
    print(f"Название: {title}")
    print(f"Год выпуска: {release_date.split('-')[0]}")
    print(f"Пользовательский рейтинг: {vote_average}/10")
    print("\nКраткий сюжет:")
    print(overview)

if __name__ == "__main__":
    movie_title = input("Введите название фильма: ")
    search_movie(movie_title)
