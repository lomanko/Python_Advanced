from application.salary import calculate_salary
from application.db.people import get_employees
from datetime import datetime
from tqdm import tqdm


def main():
    with tqdm(total=3) as py_bar:
        print(datetime.now().strftime('It is %e of %B %G. Time is %T.'))
        py_bar.update(1)
        calculate_salary()
        py_bar.update(1)
        get_employees()
        py_bar.update(1)


if __name__ == '__main__':
    main()
