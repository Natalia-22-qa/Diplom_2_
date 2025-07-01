import pytest
import allure
import requests
from urls import Urls
import data_generation


@pytest.fixture
def create_user_data():
    email = data_generation.email_generation()
    password = data_generation.password_generation()
    login_user_body = {'email': email, 'password': password}
    yield login_user_body
    
@pytest.fixture
def registration_user():
    email = data_generation.email_generation()
    password = data_generation.password_generation()
    name = data_generation.name_generation()
    create_user_body = {'email': email, 'password': password, 'name': name}
    login_user_body = {'email': email, 'password': password}
    yield create_user_body
    response = requests.post(Urls.USER_LOGIN, data=login_user_body)
    requests.delete(Urls.USER_DELETE, params=response.json()['accessToken'])

@pytest.fixture
def login_user():
    email = data_generation.email_generation()
    password = data_generation.password_generation()
    name = data_generation.name_generation()
    create_user_body = {'email': email, 'password': password, 'name': name}
    login_user_body = {'email': email, 'password': password}
    requests.post(Urls.USER_REG, data=create_user_body)
    response = requests.post(Urls.USER_LOGIN, data=login_user_body)
    yield [create_user_body, login_user_body, email, password]
    requests.delete(Urls.USER_DELETE, params=response.json()['accessToken'])
