import os

from config import ROOT_DIR
from src.JSON_Saver import JSONSaver as Js
from src.Vacancy import Vacancy

DATA_DIR = os.path.join(ROOT_DIR, "data", "vacancies.json")


def filter_vacancies(list_vacancies: list, filter_word: str) -> list:
    """Фильтрация по словам в названии вакансий"""
    filtered_vacancies = []
    for vacancy in list_vacancies:
        for key, value in vacancy.items():
            try:
                value_ = value.lower().strip()
                if filter_word in value_:
                    filtered_vacancies.append(vacancy)
                    break
            except AttributeError:
                continue

    return filtered_vacancies


# def filter_vacancies_(list_vacancies, filter_word):
#     """Фильтрация по (можно добавить фильтры по городу, опыту и т.д.)"""
#     filtered_vacancies = []
#     for vacancy in list_vacancies:
#         pass


def get_vacancies_by_salary(list_dicts: list, salary_range: str) -> list:
    """Получение вакансий по диапазону зарплат"""

    ranged_vacancies_from_salary = []
    ranged_vacancies = []
    try:
        salary_from = int(salary_range.split()[0])
        salary_to = int(salary_range.split()[-1])

    except ValueError:
        print("Не правильно указан диапазон зарплат")

    for vacancy in list_dicts:
        if salary_from <= vacancy["salary_from"]:
            ranged_vacancies_from_salary.append(vacancy)

    for vacancy in ranged_vacancies_from_salary:
        if salary_to >= vacancy["salary_to"]:
            ranged_vacancies.append(vacancy)

    return ranged_vacancies


def sort_vacancies(ranged_vacancies: list) -> list:
    """Сортировка вакансий по диапазону зарплат"""
    # sorted_vacancies = sorted(ranged_vacancies, key=lambda item: (item["salary_to"], item["salary_from"]), reverse=True)
    sorted_vacancies = sorted(ranged_vacancies, reverse=True)
    return sorted_vacancies


def get_top_vacancies(sorted_vacancies: list, top_n: int) -> list:
    """Получение топ 'N' вакансий"""
    return sorted_vacancies[:top_n]


def print_vacancies(top_vacancies: list):
    """Вывод вакансий на экран"""
    for i, top_vacancy in enumerate(top_vacancies, start=1):
        vacancy = Vacancy(top_vacancy["name"], top_vacancy["url_vacancy"], top_vacancy["salary_from"],
                          top_vacancy["salary_to"], top_vacancy["salary_currency"], top_vacancy["requirements"])
        print(f"{i}) {vacancy}")


def save_or_add(any_list: list):
    """Сохранение(пересохранение) JSON файла или добавление вакансий в JSON файл"""
    json_saver = Js(DATA_DIR)
    choice = input("Если хотите сохранить вновь полученные вакансии в JSON файл"
                   "(или перезаписать существующий файл) нажмите '1';\n"
                   "если хотите добавить полученные вакансии в существующий файл нажмите '2', "
                   "что бы пропустить нажмите 'Enter': ")
    if choice == "1":
        json_saver.save_file(any_list)
    elif choice == "2":
        json_saver.add_vacancy(any_list)
    else:
        return
