from src.utils import filter_vacancies, sort_vacancies, get_vacancies_by_salary

list_vacancies = [
    {
        'name': 'Стажер-разработчик Python',
        'area': {
            'id': '70',
            'name': 'Оренбург',
            'url': 'https://api.hh.ru/areas/70'
        },
        'salary': {
            'from': 50000,
            'to': 50000,
            'currency': 'RUR',
            'gross': True
        },
        'snippet': {
            'requirement': 'Отличные коммуникативные навыки.',
            'responsibility': 'Внедрять новые инженерные решения.'
        },
        'schedule': {
            'id': 'fullDay',
            'name': 'Полный день'
        },
        'professional_roles': [
            {
                'id': '96',
                'name': 'Программист, разработчик'
            }
        ],
        'experience': {
            'id': 'noExperience',
            'name': 'Нет опыта'
        },
        'employment': {
            'id': 'probation',
            'name': 'Стажировка'
        }
    },
    {
        'name': 'Программист Python',
        'area': {
            'id': '88',
            'name': 'Казань',
            'url': 'https://api.hh.ru/areas/88'
        },
        'salary': {
            'from': None,
            'to': 30000,
            'currency': 'RUR',
            'gross': False
        },
        'snippet': {
            'requirement': '1. Знание языка программирования Python',
            'responsibility': '1. Разработка и поддержка парсеров для сбора данных.'
        },
        'schedule': {
            'id': 'fullDay',
            'name': 'Полный день'
        },
        'professional_roles': [
            {
                'id': '96',
                'name': 'Программист, разработчик'
            }
        ],
        'experience': {
            'id': 'noExperience',
            'name': 'Нет опыта'
        },
        'employment': {
            'id': 'probation',
            'name': 'Разработчик'
        },
    }
]

filter_word = "стажер"


def test_filter_vacancies():
    assert filter_vacancies(list_vacancies, filter_word) == [
        {
            'name': 'Стажер-разработчик Python',
            'area': {
                'id': '70',
                'name': 'Оренбург',
                'url': 'https://api.hh.ru/areas/70'
            },
            'salary': {
                'from': 50000,
                'to': 50000,
                'currency': 'RUR',
                'gross': True
            },
            'snippet': {
                'requirement': 'Отличные коммуникативные навыки.',
                'responsibility': 'Внедрять новые инженерные решения.'
            },
            'schedule': {
                'id': 'fullDay',
                'name': 'Полный день'
            },
            'professional_roles': [
                {
                    'id': '96',
                    'name': 'Программист, разработчик'
                }
            ],
            'experience': {
                'id': 'noExperience',
                'name': 'Нет опыта'
            },
            'employment': {
                'id': 'probation',
                'name': 'Стажировка'
            }
        }, ]


def test_get_vacancies_by_salary():
    pass


list_salary = [(50, 100), (100, 200)]


def test_sort_vacancies():
    assert sort_vacancies(list_salary) == [(100, 200), (50, 100)]


list_salary_2 = [{"salary_from": 25, "salary_to": 40},
                 {"salary_from": 50, "salary_to": 100},
                 {"salary_from": 150, "salary_to": 200}]


def test_get_vacancies_salary():
    assert get_vacancies_by_salary(list_salary_2, "50 - 100") == [{"salary_from": 50, "salary_to": 100}]
