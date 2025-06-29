from data import *
import requests
import allure


class TestCreateOrder:
    @allure.title('Проверка создания заказа: POST /api/orders')
    @allure.step('Проверить создание заказа с авторизацией и c ингредиентами')
    def test_create_order_with_login_user_and_ingredients_success(self, login_user):
        requests.post(Urls.USER_LOGIN, data=login_user[1])
        response = requests.post(Urls.ORDER_CREATE, data=OrderData.order_body[1])
        assert response.status_code == 200 and response.json()[OrderData.success_create_order] == True
    
    @allure.step('Проверить создание заказа с авторизацией без ингредиентов')
    def test_create_order_with_login_user_without_ingredients_error(self, login_user):
        requests.post(Urls.USER_LOGIN, data=login_user[1])
        response = requests.post(Urls.ORDER_CREATE, data=OrderData.order_body[2])
        assert response.status_code == 400 and response.json() == Response.BED_REQ_CREATE_ORDER

    @allure.step('Проверить создание заказа без авторизации с ингредиентами')
    def test_create_order_without_login_user_with_ingredients_success(self):
        response = requests.post(Urls.ORDER_CREATE, data=OrderData.order_body[1])
        assert response.status_code == 200 and response.json()[OrderData.success_create_order] == True

    @allure.step('Проверить создание заказа без авторизации и без ингредиентов')
    def test_create_order_without_login_user_and_ingredients_error(self):
        response = requests.post(Urls.ORDER_CREATE, data=OrderData.order_body[2])
        assert response.status_code == 400 and response.json() == Response.BED_REQ_CREATE_ORDER

    @allure.step('Проверить создание заказа с авторизацией и неверным хешем ингредиентов')
    def test_create_order_with_login_user_and_incorrect_ingredients_error(self, login_user):
        requests.post(Urls.USER_LOGIN, data=login_user[1])
        response = requests.post(Urls.ORDER_CREATE, data=OrderData.order_body[3])
        assert response.status_code == 500

    @allure.step('Проверить создание заказа без авторизации и неверным хешем ингредиентов')
    def test_create_order_without_login_user_and_incorrect_ingredients_error(self):
        response = requests.post(Urls.ORDER_CREATE, data=OrderData.order_body[3])
        assert response.status_code == 500
