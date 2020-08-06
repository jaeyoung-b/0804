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
 
for movie in movie_list:
    movie_code = movie['code']

    import requests

    params = (
        ('code', movie_code),
        ('type', 'after'),
        ('isActualPointWriteExecute', 'false'),
        ('isMileageSubscriptionAlready', 'false'),
        ('isMileageSubscriptionReject', 'false'),
    )

    response = requests.get('https://movie.naver.com/movie/bi/mi/pointWriteFormList.nhn', params=params)

    soup = BeautifulSoup(response.text, 'html.parser')
    review_list = soup.select('body > div > div > div.score_result > ul > li')

    count = 0

    for review in review_list:
        star_score = review.select_one('div.star_score > em').text
        scorer_reple = ''

        if review.select_one(f'#_unfold_ment{count}') is None:
            score_reple = review.select_one(
                f'div.score_reple > p > span#_filtered_ment_{count}').text.strip()
       
        else:
            score_reple = review.select_one(
                f'div.score_reple > p > span#_filtered_ment_{count} > span > a')['data-src']

        print(star_score, score_reple)

        count += 1