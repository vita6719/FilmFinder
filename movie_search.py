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
     Объяснение кода:

#1. Импорт библиотек: Мы импортируем модули requests, чтобы отправлять запросы к API, и json, чтобы обрабатывать полученные данные.
   
#2. Получение ключа API: Вам необходимо заменить "ваш_ключ_API" на реальный ключ, полученный от TMDb.

#3. Функция search_movie: Эта функция принимает название фильма в качестве аргумента и выполняет поиск по API TMDb. Она отправляет запрос к URL-адресу API, получает ответ в формате JSON и извлекает нужную информацию о фильме.

#4. Обработка ответа: Если фильм не найден, выводится сообщение "Фильм не найден". Если фильм найден, то из результата извлекаются такие поля, как название, дата выхода, пользовательский рейтинг и краткий сюжет.

#5. Основной блок программы: Здесь запрашивается ввод названия фильма от пользователя, после чего вызывается функция search_movie.

### Как запустить скрипт:

#1. Откройте терминал или командную строку.
#2. Перейдите в директорию, где находится файл movie_search.py.
#3. Выполните команду:
#python movie_search.py
# Введите название фильма, когда появится соответствующий запрос.








