from abc import ABC, abstractmethod

import requests


class API(ABC):
    """Абстрактный класс для работы с API"""

    @abstractmethod
    def get_vacancies(self, keyword):
        pass


class HeadHunterAPI(API):
    """Сам класс для работы с API"""

    def __init__(self):
        self.url = "https://api.hh.ru/vacancies"

    def get_vacancies(self, keyword: str) -> list:
        """Получение вакансий с сайта"""

        # url = "https://api.hh.ru/vacancies" # старый вариант, без инит

        params = {
            "per_page": 100,
            "page": None,
            "text": keyword,
            "area": 113
        }

        response = requests.get(self.url, params=params)
        list_response = response.json()["items"]

        return list_response
