from data import *
import requests
import allure
from urls import Urls


class TestCreateOrder:
    @allure.title('Проверка создание заказа с авторизацией и c ингредиентами')
    def test_create_order_with_login_user_and_ingredients_success(self, login_user):
        with allure.step(f'1. Авторизируемся на сайте'):
            requests.post(Urls.USER_LOGIN, data=login_user[1])
        with allure.step(f'2. Отпавим POST-запрос на url {Urls.ORDER_CREATE} с ингредиентом в теле запроса'):
            response = requests.post(Urls.ORDER_CREATE, data=OrderData.order_body[1])
        with allure.step(f'3. Проверим успешное создание заказа и получение кода 200'):
            assert response.status_code == 200 and response.json()[OrderData.success_create_order] == True
    
    @allure.title('Проверка создание заказа с авторизацией без ингредиентов')
    def test_create_order_with_login_user_without_ingredients_error(self, login_user):
        with allure.step(f'1. Авторизируемся на сайте'):
            requests.post(Urls.USER_LOGIN, data=login_user[1])
        with allure.step(f'2. Отпавим POST-запрос на url {Urls.ORDER_CREATE} без ингредиента в теле запроса'):
            response = requests.post(Urls.ORDER_CREATE, data=OrderData.order_body[2])
        with allure.step(f'3. Проверим, что получили код 400 и текст ошибки {Response.BED_REQ_CREATE_ORDER}'):
            assert response.status_code == 400 and response.json() == Response.BED_REQ_CREATE_ORDER

    @allure.title('Проверка создание заказа без авторизации с ингредиентами')
    def test_create_order_without_login_user_with_ingredients_success(self):
        with allure.step(f'1. Не авторизируясь отпавим POST-запрос на url {Urls.ORDER_CREATE} с ингредиентом в теле запроса'):
            response = requests.post(Urls.ORDER_CREATE, data=OrderData.order_body[1])
        with allure.step(f'2. Проверим успешное создание заказа и получение кода 200'):
            assert response.status_code == 200 and response.json()[OrderData.success_create_order] == True

    @allure.title('Проверка создание заказа без авторизации и без ингредиентов')
    def test_create_order_without_login_user_and_ingredients_error(self):
        with allure.step(f'1. Не авторизируясь отпавим POST-запрос на url {Urls.ORDER_CREATE} без ингредиента в теле запроса'):
            response = requests.post(Urls.ORDER_CREATE, data=OrderData.order_body[2])
        with allure.step(f'2. Проверим, что получили код 400 и текст ошибки {Response.BED_REQ_CREATE_ORDER}'):
            assert response.status_code == 400 and response.json() == Response.BED_REQ_CREATE_ORDER

    @allure.title('Проверка создание заказа с авторизацией и неверным хешем ингредиентов')
    def test_create_order_with_login_user_and_incorrect_ingredients_error(self, login_user):
        with allure.step(f'1. Авторизируемся на сайте'):
            requests.post(Urls.USER_LOGIN, data=login_user[1])
        with allure.step(f'2. Отпавим POST-запрос на url {Urls.ORDER_CREATE} с неверным хешем ингредиента в теле запроса'):
            response = requests.post(Urls.ORDER_CREATE, data=OrderData.order_body[3])
        with allure.step(f'3. Проверим, что получили код 500'):
            assert response.status_code == 500

    @allure.title('Проверка создание заказа без авторизации и неверным хешем ингредиентов')
    def test_create_order_without_login_user_and_incorrect_ingredients_error(self):
        with allure.step(f'1. Не авторизируясь отпавим POST-запрос на url {Urls.ORDER_CREATE} с неверным хешем ингредиента в теле запроса'):
            response = requests.post(Urls.ORDER_CREATE, data=OrderData.order_body[3])
        with allure.step(f'2. Проверим, что получили код 500'):
            assert response.status_code == 500
