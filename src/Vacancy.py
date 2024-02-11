class Vacancy:
    """Класс для работы с вакансией"""

    def __init__(self, title_vacancy, url_vacancy, salary_from, salary_to, salary_currency, requirements):
        self.title_vacancy = title_vacancy
        self.url_vacancy = url_vacancy
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.salary_currency = salary_currency
        self.requirements = requirements

    def __repr__(self):
        return f'Название вакансии: {self.title_vacancy}\n' \
               f'Ссылка на вакансию: {self.url_vacancy}\n' \
               f'Зарплата от: {self.salary_from}\n' \
               f'Зарплата до: {self.salary_to}\n' \
               f'Валюта: {self.salary_currency}\n' \
               f'Требования: {self.requirements}\n' \


    def __str__(self):
        return f'Название вакансии: {self.title_vacancy}\n' \
               f'Ссылка на вакансию: {self.url_vacancy}\n' \
               f'Зарплата от: {self.salary_from}\n' \
               f'Зарплата до: {self.salary_to}\n' \
               f'Валюта: {self.salary_currency}\n' \
               f'Требования: {self.requirements}\n' \


    def to_dict(self):
        """Преобразование в словарь"""
        return {
            "name": self.title_vacancy,
            "url_vacancy": self.url_vacancy,
            "salary_from": self.salary_from,
            "salary_to": self.salary_to,
            "salary_currency": self.salary_currency,
            "requirements": self.requirements
        }

    # def __gt__(self, other):
    #     return int(self.salary_from) > int(other.salary_from)

    # def __ge__(self, other):
    #     return int(self.salary_from) >= int(other.salary_from)

    def __lt__(self, other):
        return int(self.salary_from) < int(other.salary_from)

    # def __le__(self, other):
    #     return int(other.salary_from) <= int(self.salary_from)

    # def __eq__(self, other):
    #     return int(self.salary_from) == int(other.salary_from)


class Vacancies(Vacancy):
    """Класс для работы с вакансиями"""
    
    @staticmethod
    def add_list_dicts(any_list: list) -> list:
        """Преобразование списка в список словарей"""
        list_dicts = []
        for vacancy in any_list:
            list_dicts.append(vacancy.to_dict())

        return list_dicts

    @classmethod
    def format_list(cls, list_response: list) -> list:
        """
        Преобразование набора данных из JSON в список объектов
        """

        formatted_list = []

        for one_vacancy in list_response:
            title_vacancy = one_vacancy["name"]
            url_vacancy = one_vacancy["alternate_url"]
            if not (one_vacancy["salary"] is None):
                if not (one_vacancy["salary"]["from"] is None):
                    salary_from = one_vacancy["salary"]["from"]
                else:
                    salary_from = 0
                if not (one_vacancy["salary"]["to"] is None):
                    salary_to = one_vacancy["salary"]["to"]
                else:
                    salary_to = 0
                salary_currency = one_vacancy["salary"]["currency"]
            else:
                salary_from = 0
                salary_to = 0
                salary_currency = "Не указано"
            requirements = one_vacancy["snippet"]["requirement"]
            vacancy = cls(title_vacancy, url_vacancy, salary_from, salary_to, salary_currency, requirements)
            formatted_list.append(vacancy)

        return formatted_list

    @classmethod
    def format_list_exemplar(cls, list_response: list) -> list:
        """
        Преобразование списка словарей в список экземпляров
        """

        formatted_list_exemplar = []

        for one_vacancy in list_response:
            title_vacancy = one_vacancy["name"]
            url_vacancy = one_vacancy["url_vacancy"]
            salary_from = one_vacancy["salary_from"]
            salary_to = one_vacancy["salary_to"]
            salary_currency = one_vacancy["salary_currency"]
            requirements = one_vacancy["requirements"]
            vacancy = cls(title_vacancy, url_vacancy, salary_from, salary_to, salary_currency, requirements)
            formatted_list_exemplar.append(vacancy)

        return formatted_list_exemplar
