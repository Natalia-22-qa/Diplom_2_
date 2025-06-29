import pytest
from data import *
import requests
import allure


class TestCreateUser:
    @allure.title('Проверка создания пользователя: POST /api/auth/register')
    @allure.step('Проверить, что новый пользователь регистрируется в системе')
    def test_create_user_success(self, registration_user):
        response = requests.post(Urls.USER_REG, data=registration_user)
        assert response.status_code == 200 and User.token in response.json()
   
    @allure.step('Проверить появление ошибки при создании одинаковых пользователей')
    def test_create_user_clone_error(self, login_user):
        response = requests.post(Urls.USER_REG, data=login_user[0])
        assert response.status_code == 403 and response.json() == Response.CONFLICT_CREATE_USER

    @allure.step('Проверить появление ошибки при отсутствии обязательного поля')
    @pytest.mark.parametrize('user_data', User.reg_data)
    def test_create_user_without_required_field_error(self, user_data):
        response = requests.post(Urls.USER_REG, data=user_data)
        assert response.status_code == 403 and response.json() == Response.BED_REQ_CREATE_USER
