import json
from abc import ABC, abstractmethod

from src.Vacancy import Vacancy


class AbcJSONSaver(ABC):
    """Абстрактный класс для работы с JSON файлом"""

    def __init__(self, path):
        self.path = path

    @abstractmethod
    def save_file(self, path, data):
        pass

    @abstractmethod
    def read_file(self, data):
        pass

    @abstractmethod
    def add_vacancy(self, path, vacancy):
        pass

    @abstractmethod
    def delete_vacancy(self, path, vacancy):
        pass


class JSONSaver(AbcJSONSaver, Vacancy):
    """Сам класс для работы с JSON файлом"""

    @classmethod
    def save_file(cls, path: str, data: list):
        """
        Сохранение файла
        """
        with open(path, "w", encoding="utf-8") as file:
            file.write(json.dumps(data, indent=2, ensure_ascii=False))

    @classmethod
    def read_file(cls, path: str):
        """
        Чтение файла
        """
        with open(path, "r", encoding="utf-8") as file:
            old_list = json.load(file)
            return old_list

    @classmethod
    def add_vacancy(cls, path: str, data: list):
        """
        Добавление списка вакансий в json файл
        """
        old_list = cls.read_file(path)
        new_list = data + old_list

        cls.save_file(path, new_list)

    @classmethod
    def delete_vacancy(cls, path: str, vacancy: str):
        """
        Удаление вакансии по названию вакансии
        """
        new_list = []

        old_list = cls.read_file(path)

        for one_vacancy in old_list:
            if vacancy != one_vacancy["name"]:
                new_list.append(one_vacancy)

        cls.save_file(path, new_list)
