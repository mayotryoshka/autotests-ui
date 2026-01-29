def test_first_try():
    print("Hello World!")

def test_assert_positive_case():  # Новый тест, который проверяет положительный кейс
    assert (2 + 2) == 4  # Ожидается, что тест пройдет
    assert (3 + 3) == 6


def test_assert_negative_case():  # Новый тест, который проверяет негативный кейс
    assert (2 + 2) != 5, '2 + 2 != 5'  # Тут должна быть ошибка