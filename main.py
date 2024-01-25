from vacancies.catalog import Catalog


def main():
    cat = Catalog()
    user = input('Введите профессию\n----> ')

    cat.upload_vacancies(user)
    cat.save_to_file()

    data = cat.read_from_file()

    while True:
        try:
            user_filter = int(input('Введите критерий фильтрации:\n'
                                    'Минимальная зарплата - 1\n'
                                    'Максимальная зарплата - 2\n'
                                    'Все данные - 3\n'
                                    'Для выхода: 0\n---> '))
            break  # если ввод корректен, выходим из цикла
        except ValueError:
            print("Ошибка: Введите число от 1 до 3\n")
    for vac in data:

        if user_filter == 1:
            print(f"Должность: {vac['job_title']}\n"
                  f"Компания: {vac['company']}\n"
                  f"Минимальная зарплата: {vac['salary_min']}\n"
                  f"Источник: {vac['source']}\n")
        elif user_filter == 2:
            print(f"Должность: {vac['job_title']}\n"
                  f"Компания: {vac['company']}\n"
                  f"Максимальная зарплата: {vac['salary_max']}\n"
                  f"Источник: {vac['source']}\n")
        elif user_filter == 3:
            print(f"Должность: {vac['job_title']}\n"
                  f"Компания: {vac['company']}\n"
                  f"Минимальная зарплата: {vac['salary_min']}\n"
                  f"Максимальная зарплата: {vac['salary_max']}\n"
                  f"url: {vac['url']}\n"
                  f"Источник: {vac['source']}\n"
                  f"Описание: {vac['requirements'].replace('<highlighttext>', '')}, {vac['source']}\n")
        elif user_filter == 0:
            print('Вы завершили программу')
            break
        else:
            print("Не верно указаны данные для фильтрации")
            break


if __name__ == '__main__':
    main()
