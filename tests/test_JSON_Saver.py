import os
from config import ROOT_DIR
from src.JSON_Saver import JSONSaver, AbcJSONSaver

DATA_DIR = os.path.join(ROOT_DIR, "data", "test_vacancies.json")

json_saver = JSONSaver(DATA_DIR)

data = [1, 2, 3]


def test_json_saver_issubclass():
    assert issubclass(JSONSaver, AbcJSONSaver)


def test_save_file():
    assert json_saver.save_file(data) is None


def test_read_file():
    assert json_saver.read_file() == [1, 2, 3]


def test_add_vacancy():
    assert json_saver.add_vacancy([4]) is None
