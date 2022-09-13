from habr_scrapping import HabrScrapper, generate_headers
from text_refactor import lemmatize_list
from tabulate import tabulate

if __name__ == '__main__':
    headers = generate_headers('mac')
    Scrapper = HabrScrapper(headers)
    keywords = ['ноутбуком', 'продуктов']

    # поиск статей с ключевыми словами в превью
    articles_df_preview = Scrapper.get_articles_df(keywords=keywords, keyword_type='preview')
    print(f'Список статей с ключевыми словами {lemmatize_list(keywords)} в превью:')
    print(tabulate(articles_df_preview[['title', 'date', 'link']], headers='keys', tablefmt='psql'))

    print()
    print()

    # поиск статей с ключевыми словами в тексте статьи
    articles_df_text = Scrapper.get_articles_df(keywords=keywords, keyword_type='text')
    print(f'Список статей с ключевыми словами {lemmatize_list(keywords)} в тексте статьи:')
    print(tabulate(articles_df_text[['title', 'date', 'link']], headers='keys', tablefmt='psql'))
