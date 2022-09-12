import numpy as np
import pandas as pd

if __name__ == '__main__':
    # чтение файла csv
    column_names = ['lastname', 'firstname', 'surname', 'organization', 'position', 'phone', 'email']
    df = pd.read_csv('phonebook_raw.csv', usecols=column_names)

    # помещаем фамилию, имя и отчество в корректные колонки
    # Задание 1
    df['full_name'] = df['lastname'].astype(str).str.cat(df[['firstname', 'surname']], sep=' ', na_rep='').str.strip()
    df[['lastname', 'firstname', 'surname']] = df['full_name'].str.split(' ', expand=True, n=2)
    df = df.replace(r'^\s*$', np.nan, regex=True)
    df = df.drop('full_name', axis=1)

    # объединение дублирующихся строк (дубликат, если совпадает имя и фамилия)
    # Задание 3
    df = df.groupby(['lastname', 'firstname']).agg('last').reset_index()

    # изменение записи телефонов
    # Задание 2
    pattern = r"(\+7|8)?(\s|-|\()*(\d{3})(\s|-|\))*(\d{3})(\s*|-)*(\d{2})(\s|-)*(\d{2})(\s|-|\()*(доб.)?(\s|-|\()*(\d{4})*(\))*"
    new_pattern = r"+7(\3)\5-\7-\9 \11\13"
    df['phone'] = df['phone'].replace(pattern, new_pattern, regex=True).str.strip()

    # сохранение в новый csv файл
    df.to_csv('new_phonebook_raw.csv', index=False)
