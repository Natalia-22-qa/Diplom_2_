import data_generation

class Urls:
    URL = 'https://stellarburgers.nomoreparties.site'
    USER_REG = f'{URL}/api/auth/register'
    USER_LOGIN = f'{URL}/api/auth/login'
    USER_DELETE = f'{URL}/api/auth/user'
    ORDER_CREATE = f'{URL}/api/orders'

class OrderData:
    order_body = {
        1: {'ingredients': ["61c0c5a71d1f82001bdaaa6d"]}, # корректный ингредиент
        2: {'ingredients': []},                           # без ингредиента
        3: {'ingredients': ["61c0c5a71d1f8"]}             # неверный хеш ингредиента
    }
    success_create_order = 'success'

class Response:
    CONFLICT_CREATE_USER = {'success': False, 'message': 'User already exists'}
    BED_REQ_CREATE_USER = {'success': False, 'message': 'Email, password and name are required fields'}
    BED_REQ_LOGIN_USER = {'success': False, 'message': 'email or password are incorrect'}
    BED_REQ_CREATE_ORDER = {'success': False, 'message': 'Ingredient ids must be provided'}

class User:
    reg_data = [{'email': data_generation.email_generation(), 'name': data_generation.name_generation()},
                {'password': data_generation.password_generation(), 'name': data_generation.name_generation()},
                {'email': data_generation.email_generation(), 'password': data_generation.password_generation()}]
    token = 'accessToken'