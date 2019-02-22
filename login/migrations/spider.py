# coding:utf-8

import requests, os, sys, django
from bs4 import BeautifulSoup
from django.core.wsgi import get_wsgi_application

sys.path.extend([r'D:/pycharm/django1/django1', ])
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django1.settings")
application = get_wsgi_application()
django.setup()
from login.models import Movie

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Host': 'maoyan.com',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
}


def insert_data():
    url = 'https://maoyan.com/films?showType=3&yearId=12'
    #'https://maoyan.com/films?showType=3&yearId=14'
    wbdata = requests.get(url, headers=headers)
    soup = BeautifulSoup(wbdata.content, 'html.parser')
    movie_list = soup.select('div.movie-item > a')
    for movie in movie_list:
        m_url = 'http://maoyan.com' + movie.get('href')
        m_data = requests.get(m_url, headers=headers)
        m_soup = BeautifulSoup(m_data.content, 'html.parser')
        title = m_soup.select_one('div.movie-brief-container > h3.name').get_text()
        cate = m_soup.select("div.movie-brief-container > ul > li")[0].get_text()
        date = m_soup.select("div.movie-brief-container > ul > li")[2].get_text()[0:10]
        img = m_soup.select_one('div.avatar-shadow > img').get('src')
        print(title, cate, date, img)
        insertdata = Movie.objects.get_or_create(
            name=title,
            movie_cate=cate,
            movie_img=img,
            release_date=date
        )


if __name__ == '__main__':
    insert_data()