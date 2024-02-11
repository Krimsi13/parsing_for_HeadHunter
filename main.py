import os

from config import ROOT_DIR
from src.API import HeadHunterAPI
from src.JSON_Saver import JSONSaver
from src.Vacancy import Vacancies
from src.utils import filter_vacancies, get_vacancies_by_salary, sort_vacancies, get_top_vacancies, print_vacancies, \
    save_or_add

DATA_DIR = os.path.join(ROOT_DIR, "data", "vacancies.json")

hh_api = HeadHunterAPI()


def user_interaction():
    """Функция для взаимодействия с пользователем"""
    search_query = input("Введите поисковый запрос: ").capitalize()
    hh_vacancies = hh_api.get_vacancies(search_query)
    filter_word = input("Введите ключевое слово для фильтрации вакансий(например 'стажер'/'junior'),"
                        "что бы пропустить этот фильтр нажмите 'Enter': ").lower()
    filtered_vacancies = filter_vacancies(hh_vacancies, filter_word)

    if not filtered_vacancies:
        print("Нет вакансий, соответствующих заданным критериям.")
        return

    format_list_filtered_vacancies = Vacancies.format_list(filtered_vacancies)
    list_dicts = Vacancies.add_list_dicts(format_list_filtered_vacancies)

    format_list_for_print = input("Если хотите посмотреть полученные вакансии нажмите '1', "
                                  "что бы пропустить нажмите 'Enter': ")
    if format_list_for_print == "1":
        print_vacancies(list_dicts)

    json_saver = JSONSaver(DATA_DIR)

    save_or_add(list_dicts)

    salary_range = input("Введите диапазон зарплат(Пример: 100000 - 150000): ")  # Пример: 100000 - 150000
    ranged_vacancies = get_vacancies_by_salary(list_dicts, salary_range)
    format_ranged_vacancies = Vacancies.format_list_exemplar(ranged_vacancies)
    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    sorted_vacancies = sort_vacancies(format_ranged_vacancies)
    sorted_vacancies_list_dicts = Vacancies.add_list_dicts(sorted_vacancies)
    top_vacancies = get_top_vacancies(sorted_vacancies_list_dicts, top_n)
    print_vacancies(top_vacancies)

    save_or_add(top_vacancies)
        
    read_json_file = input("Если хотите посмотреть содержание существующего JSON файла нажмите '1': "
                           "что бы пропустить нажмите 'Enter': ")
    if read_json_file == "1":
        for_display = json_saver.read_file()
        print_vacancies(for_display)

    while True:
        del_vacancy_from_file = input("Если хотите удалить вакансию по названию из JSON файла нажмите '1': ")
        if del_vacancy_from_file == "1":
            name_vacancy = input("Введите назание вакансии: ")
            json_saver.delete_vacancy(name_vacancy)
        else:
            break


if __name__ == "__main__":
    user_interaction()
