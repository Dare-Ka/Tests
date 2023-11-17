import requests
import config


# Задание «Проверка логина и пароля»
def check_auth(login: str, password: str):

    if login == 'admin' and password == 'password':
        result = 'Добро пожаловать'
    else:
        result = 'Доступ ограничен'

    return result


# Задание «Проверка возраста»
def check_age(age: int):

    if age >= 18:
        result = 'Доступ разрешён'
    else:
        result = 'Доступ запрещён'

    return result


# Задание «Знакомство»
def solve(boys: list, girls: list):
    result = ""

    if len(boys) == len(girls):
        for boy, girl in list(
                zip(sorted(boys), sorted(girls))):
            result += f"{boy} и {girl}, "
    else:
        result = "Кто-то может остаться без пары!  "
    return result[0:-2]


def create_folder(path):
    url = 'https://cloud-api.yandex.net/v1/disk/resources'
    headers = {
        'Authorization': f'OAuth {config.token_Yandex}'
    }
    params = {'path': path}
    response = requests.put(url, headers=headers, params=params)
    return response.status_code


def get_folder(path):
    url = 'https://cloud-api.yandex.net/v1/disk/resources'
    headers = {
        'Authorization': f'OAuth {config.token_Yandex}'
    }
    params = {'path': path}
    response = requests.get(url, headers=headers, params=params)
    return response.status_code

print(create_folder('test_folder'))
print(get_folder('test_folder'))
