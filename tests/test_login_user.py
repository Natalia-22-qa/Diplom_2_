from data import *
import requests
import allure


class TestLoginUser:
    @allure.title('Проверка авторизации пользователя: POST /api/auth/login')
    @allure.step('Проверить, что пользователь авторизировался')
    def test_login_user_success(self, login_user):
        response = requests.post(Urls.USER_LOGIN, data=login_user[1])
        assert response.status_code == 200 and User.token in response.json()
    
    @allure.step('Проверить появление ошибки при авторизации с неверными данными')
    def test_login_with_error_data_user_error(self, create_user_data):
        response = requests.post(Urls.USER_LOGIN, data=create_user_data)
        assert response.status_code == 401 and response.json() == Response.BED_REQ_LOGIN_USER

    @allure.step('Проверить появление ошибки при авторизации без логина')
    def test_login_user_without_login_error(self, login_user):
        login_user_body = {'email': '', 'password': login_user[2]}
        response = requests.post(Urls.USER_LOGIN, data=login_user_body)
        assert response.status_code == 401 and response.json() == Response.BED_REQ_LOGIN_USER

    @allure.step('Проверить появление ошибки при авторизации без пароля')
    def test_login_user_without_password_error(self, login_user):
        login_user_body = {'email': login_user[3], 'password': ''}
        response = requests.post(Urls.USER_LOGIN, data=login_user_body)
        assert response.status_code == 401 and response.json() == Response.BED_REQ_LOGIN_USER
