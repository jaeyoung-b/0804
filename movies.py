import requests
from bs4 import BeautifulSoup


movie_url = "https://movie.naver.com/movie/running/current.nhn"
response = requests.get(movie_url)
soup = BeautifulSoup(response.text, 'html.parser')

movie_a = soup.select('#content > div.article > div:nth-child(1) > div.lst_wrap > ul > li')

movie_list = []

for movie in movie_a:
    a_tag = movie.select_one('dl > dt > a')

    movie_title = a_tag.text
    movie_code = a_tag['href'].split('=')[1]

    movie_data = {
        'title' : movie_title,
        'code' : movie_code
    }

    movie_list.append(movie_data)

print(movie_list)