import requests

from src.API import HeadHunterAPI

hh_api = HeadHunterAPI()


def test_get_vacancies():
    response = hh_api.get_vacancies("python")
    assert isinstance(response, list)
    assert len(response) > 0
