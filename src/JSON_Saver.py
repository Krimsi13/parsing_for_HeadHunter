import json
from abc import ABC, abstractmethod

# from src.Vacancy import Vacancy


class AbcJSONSaver(ABC):
    """Абстрактный класс для работы с JSON файлом"""

    @abstractmethod
    def save_file(self, data):
        pass

    @abstractmethod
    def read_file(self):
        pass

    @abstractmethod
    def add_vacancy(self, vacancy):
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy):
        pass


class JSONSaver(AbcJSONSaver):
    """Сам класс для работы с JSON файлом"""
    def __init__(self, path):
        self.path = path

    def save_file(self, data: list):
        """
        Сохранение файла
        """
        with open(self.path, "w", encoding="utf-8") as file:
            file.write(json.dumps(data, indent=2, ensure_ascii=False))

    def read_file(self):
        """
        Чтение файла
        """
        with open(self.path, "r", encoding="utf-8") as file:
            old_list = json.load(file)
            return old_list

    def add_vacancy(self, data: list):
        """
        Добавление списка вакансий в json файл
        """
        old_list = self.read_file()
        new_list = data + old_list

        self.save_file(new_list)

    def delete_vacancy(self, vacancy: str):
        """
        Удаление вакансии по названию вакансии
        """
        new_list = []

        old_list = self.read_file()

        for one_vacancy in old_list:
            if vacancy != one_vacancy["name"]:
                new_list.append(one_vacancy)

        self.save_file(new_list)
