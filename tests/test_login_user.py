from data import *
import requests
import allure
from urls import Urls


class TestLoginUser:
    @allure.title('Проверка успешной авторизации пользователя авторизировался')
    def test_login_user_success(self, login_user):
        with allure.step(f'1. Отпавим POST-запрос на url {Urls.USER_LOGIN} с данными зарегистрированного пользователя'):
            response = requests.post(Urls.USER_LOGIN, data=login_user[1])
        with allure.step(f'2. Проверим, что получили код 200, а в теле ответа есть токен'):
            assert response.status_code == 200 and User.token in response.json()
    
    @allure.title('Проверка появления ошибки при авторизации с неверными данными')
    def test_login_with_error_data_user_error(self, create_user_data):
        with allure.step(f'1. Отпавим POST-запрос на url {Urls.USER_LOGIN} с данными незарегистрированного пользователя'):
            response = requests.post(Urls.USER_LOGIN, data=create_user_data)
        with allure.step(f'2. Проверим, что получили код 401 и текст ошибки {Response.BED_REQ_LOGIN_USER}'):
            assert response.status_code == 401 and response.json() == Response.BED_REQ_LOGIN_USER

    @allure.title('Проверка появления ошибки при авторизации без логина')
    def test_login_user_without_login_error(self, login_user):
        with allure.step(f'1. Отпавим POST-запрос на url {Urls.USER_LOGIN} без логина в теле запроса'):
            login_user_body = {'email': '', 'password': login_user[2]}
            response = requests.post(Urls.USER_LOGIN, data=login_user_body)
        with allure.step(f'2. Проверим, что получили код 401 и текст ошибки {Response.BED_REQ_LOGIN_USER}'):
            assert response.status_code == 401 and response.json() == Response.BED_REQ_LOGIN_USER

    @allure.title('Проверка появления ошибки при авторизации без пароля')
    def test_login_user_without_password_error(self, login_user):
        with allure.step(f'1. Отпавим POST-запрос на url {Urls.USER_LOGIN} без пароля в теле запроса'):
            login_user_body = {'email': login_user[3], 'password': ''}
            response = requests.post(Urls.USER_LOGIN, data=login_user_body)
        with allure.step(f'2. Проверим, что получили код 401 и текст ошибки {Response.BED_REQ_LOGIN_USER}'):
            assert response.status_code == 401 and response.json() == Response.BED_REQ_LOGIN_USER
