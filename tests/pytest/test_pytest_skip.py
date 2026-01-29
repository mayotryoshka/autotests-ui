import pytest

@pytest.mark.skip(reason="Фича в разработке") # Маркировка пропустит этот тест
def test_feature_in_development():
    pass