import pytest

# Фикстура для очистки данных из базы данных
@pytest.fixture
def clear_books_database() -> None:
    print("[FIXTURE] Удаляем все данные из базы данных")


# Фикстура для заполнения данных в базу данных
@pytest.fixture
def fill_books_database() -> None:
    print("[FIXTURE] Создаем новые данные в базе данных")

@pytest.mark.usefixtures('fill_books_database')
def test_read_all_books_in_library(clear_books_database):
    print("Reading all books")

# Можно писать по одной фикстуре за раз в usefixtures, последовательность важна, если играет роль
@pytest.mark.usefixtures(
    'clear_books_database',
    'fill_books_database',
)
class TestLibrary:
    def test_read_book_from_library(self):
        ...

    def test_delete_book_from_library(self):
        ...