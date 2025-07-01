import pytest
from data import *
import requests
import allure
from urls import Urls


class TestCreateUser:
    @allure.title('Проверка успешной регистрации нового пользователя в системе')
    def test_create_user_success(self, registration_user):
        with allure.step(f'1. Отпавим POST-запрос на url {Urls.USER_REG} с корректными данными'):
            response = requests.post(Urls.USER_REG, data=registration_user)
        with allure.step(f'2. Проверим, что получили код 200, а в теле ответа есть токен'):
            assert response.status_code == 200 and User.token in response.json()
   
    @allure.title('Проверка появления ошибки при создании одинаковых пользователей')
    def test_create_user_clone_error(self, login_user):
        with allure.step(f'1. Отпавим POST-запрос на url {Urls.USER_REG} с данными уже зарегистрированного пользователя'):
            response = requests.post(Urls.USER_REG, data=login_user[0])
        with allure.step(f'2. Проверим, что получили код 403 и текст ошибки {Response.CONFLICT_CREATE_USER}'):
            assert response.status_code == 403 and response.json() == Response.CONFLICT_CREATE_USER

    @allure.title('Проверка появления ошибки при отсутствии обязательного поля')
    @pytest.mark.parametrize('user_data', User.reg_data)
    def test_create_user_without_required_field_error(self, user_data):
        with allure.step(f'1. Отпавим POST-запросы на url {Urls.USER_REG} поочередно без одного из полей'):
            response = requests.post(Urls.USER_REG, data=user_data)
        with allure.step(f'2. Проверим, что получили код 403 и текст ошибки {Response.BED_REQ_CREATE_USER}'):
            assert response.status_code == 403 and response.json() == Response.BED_REQ_CREATE_USER
