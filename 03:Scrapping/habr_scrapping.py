import requests
from fake_headers import Headers
from bs4 import BeautifulSoup
import pandas as pd
from text_refactor import lemmatize_list, get_list_from_text


def generate_headers(os):  # генерация headers
    headers = Headers(os=os, headers=True).generate()
    return headers


class HabrScrapper:

    base_url = 'https://habr.com'
    url = base_url + '/ru/all/'

    def __init__(self, headers):
        self.headers = headers

    def parse_html(self, url):  # скраппинг страницы
        response = requests.get(url, headers=self.headers)
        text = response.text
        soup = BeautifulSoup(text, 'html.parser')
        return soup

    def get_article_text(self, article_url):  # получает текст статьи по её ссылке
        soup = self.parse_html(article_url)
        text_article = soup.find('div', class_='tm-article-body').text
        return text_article

    def get_articles_df(self, keywords=None, keyword_type='preview'):
        """
        Функция формирует датафрейм:
        - title - название статьи;
        - preview - текст превью статьи;
        - link - ссылка на полную статью;
        - article_text - полные текст статьи.

        Если задан параметр keywords (список), то функция ищет ключевые слова
        в превью (keyword_type='preview') или в тексте (keyword_type='text') статьи.
        """
        soup = self.parse_html(self.url)
        articles = soup.find_all('div', class_='tm-article-snippet')  # блок с данными о статье
        habr_news = pd.DataFrame()  # формируем пустой data frame

        for article in articles:
            article_title = article.find(class_='tm-article-snippet__title-link').text  # название статьи
            article_preview = article.find(class_='tm-article-body tm-article-snippet__lead').text  # превью статьи
            article_link = article.find(class_='tm-article-snippet__readmore').get('href')  # ссылка статьи
            article_text = self.get_article_text(self.base_url + article_link)  # текст статьи
            date = article.find('span', class_='tm-article-snippet__datetime-published').time.get('title')
            row = {'title': article_title,
                   'date': date,
                   'preview': article_preview,
                   'link': self.base_url + article_link,
                   'article_text': article_text}

            if keywords is None:  # проверка заданы ли ключевые слова
                habr_news = pd.concat([habr_news, pd.DataFrame([row])]).reset_index(drop=True)
            else:
                keywords_lemm = lemmatize_list(keywords)  # приводим ключевые слова к их леммам
                if keyword_type == 'preview':  # проверка превью статьи
                    words = get_list_from_text(article_preview)  # список слов в превью
                    words_lemm = lemmatize_list(words)  # список слов в превью в виде леммы слов
                    same_words = set(keywords_lemm) & set(words_lemm)  # пересечение списков ключевых слов и слов из превью
                    if same_words:  # если есть пересечение ключевых слов, то берем статью
                        habr_news = pd.concat([habr_news, pd.DataFrame([row])]).reset_index(drop=True)
                elif keyword_type == 'text':  # проверка текста статьи
                    words = get_list_from_text(article_text)  # список слов в тексте статьи
                    words_lemm = lemmatize_list(words)  # список слов в тексте статьи в виде леммы слов
                    same_words = set(keywords_lemm) & set(words_lemm)  # пересечение списков ключевых слов и слов из текста статьи
                    if same_words:  # если есть пересечение ключевых слов, то берем статью
                        habr_news = pd.concat([habr_news, pd.DataFrame([row])]).reset_index(drop=True)
        return habr_news
