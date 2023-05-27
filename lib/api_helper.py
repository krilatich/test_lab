import requests
from requests import Response, get, post

BASE_URL = 'http://localhost:5000/'


def get_form():
    return requests.get(BASE_URL)


def post_form(data):
    return requests.post(f'{BASE_URL}', data={'data': data})

