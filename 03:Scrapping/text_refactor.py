import pymorphy2
import re

morph = pymorphy2.MorphAnalyzer()


def lemmatize_list(list_):
    """
    Функция превращает все слова в списке в их леммы.
    """
    lemmatize_words = [morph.parse(word)[0].normal_form for word in list_]
    return lemmatize_words


def get_list_from_text(text):
    """
    Функция превращает текст в список, убирая все символы, кроме букв и цифр.
    """
    words = re.sub('[\W_]+', ' ', text).split()
    return words
