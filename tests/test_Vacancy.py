from src.Vacancy import Vacancy, Vacancies

vacancy = Vacancy("Python Developer", "https://hh.ru/vacancy/92765024", 100000,
                  150000, "RUR",
                  "Увлеченность IT - тематикой и стремление к развитию в этом направлении. Основы ООП,"
                  " простейшие алгоритмы.")

vacancy_2 = Vacancy("Python Developer", "https://hh.ru/vacancy/92765024", 50000,
                    100000, "RUR",
                    "Увлеченность IT - тематикой и стремление к развитию в этом направлении. Основы ООП,"
                    " простейшие алгоритмы.")

vacancies = Vacancies("Python Developer", "https://hh.ru/vacancy/92765024", 100000,
                      150000, "RUR",
                      "Увлеченность IT - тематикой и стремление к развитию в этом направлении. Основы ООП,"
                      " простейшие алгоритмы.")


def test_to_dict():
    assert vacancy.to_dict() == {
        "name": "Python Developer",
        "url_vacancy": "https://hh.ru/vacancy/92765024",
        "salary_from": 100000,
        "salary_to": 150000,
        "salary_currency": "RUR",
        "requirements": "Увлеченность IT - тематикой и стремление к развитию в этом направлении. Основы ООП,"
                        " простейшие алгоритмы."
    }


def test_repr_and_str():
    assert repr(vacancy) == ('Название вакансии: Python Developer\n'
                             'Ссылка на вакансию: https://hh.ru/vacancy/92765024\n'
                             'Зарплата от: 100000\n'
                             'Зарплата до: 150000\n'
                             'Валюта: RUR\n'
                             'Требования: Увлеченность IT - тематикой и стремление к развитию в этом '
                             'направлении. Основы ООП, простейшие алгоритмы.\n')

    assert str(vacancy) == ('Название вакансии: Python Developer\n'
                            'Ссылка на вакансию: https://hh.ru/vacancy/92765024\n'
                            'Зарплата от: 100000\n'
                            'Зарплата до: 150000\n'
                            'Валюта: RUR\n'
                            'Требования: Увлеченность IT - тематикой и стремление к развитию в этом '
                            'направлении. Основы ООП, простейшие алгоритмы.\n')


def test_lt():
    assert (vacancy < vacancy_2) == False


any_list = [vacancy, vacancy_2]
list_dicts = vacancies.add_list_dicts(any_list)
list_exemplar = vacancies.format_list_exemplar(list_dicts)


def test_add_list_dicts():
    assert isinstance(list_dicts[0], dict)


def test_format_list_exemplar():
    assert isinstance(list_exemplar[0], object)

