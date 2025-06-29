from faker import Faker

fake = Faker()
fakeRU = Faker(locale='ru_RU')


def email_generation():
    email = fake.free_email()
    return email

def password_generation():
    password = fake.random_number(6)
    return password

def name_generation():
    name = fakeRU.first_name()
    return name
