import pytest
from main import check_auth, check_age, solve, create_folder, get_folder


@pytest.mark.parametrize('login, password, expected', (
    ['admin', 'password', 'Добро пожаловать'],
    ['user', 'password', 'Доступ ограничен'],
    ['admin', 'password', 'Добро пожаловать'],
    ['user', 'wrong', 'Доступ ограничен'],
    )
)
def test_check_auth(login, password, expected):
    login = 'admin'
    password = 'password'
    result = check_auth(login, password)
    assert result == expected



@pytest.mark.parametrize('age, expected', (
    [18, 'Доступ разрешён'],
    [17, 'Доступ запрещён'],
    [20, 'Доступ разрешён'],
    [19, 'Доступ запрещён'],
    )
)
def test_check_age(age, expected):
    result = check_age(age)
    assert result  == expected


@pytest.mark.parametrize('boys, girls, expected', (
    [['Peter', 'Alex', 'John', 'Arthur', 'Richard'],
     ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha'],
     'Alex и Emma, Arthur и Kate, John и Kira, Peter и Liza, Richard и Trisha'],
    [['Peter', 'Alex', 'John', 'Arthur', 'Richard'],
     ['Kate', 'Liza', 'Kira', 'Emma'],
     'Кто-то может остаться без пары!'],
    [['Peter', 'Alex', 'John', 'Arthur'],
     ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha'],
     'Кто-то может остаться без пары!'],
    )
)
def test_solve(boys, girls, expected):
    result = solve(boys, girls)
    assert result == expected

@pytest.mark.parametrize('path, expected', (
    ['test_folder', 201],
    ['test_folder', 409]
    )
)
def test_create_folder(path, expected):
    result = create_folder(path)
    assert result == expected

@pytest.mark.parametrize('path, expected', (
    ['test_folder', 200],
    ['test_folder', 400],
    ['failed_folder', 404]
    )
)
def test_get_folder(path, expected):
    result = get_folder(path)
    assert result == expected


