import pytest

from src.repositories.memory import store


@pytest.fixture(autouse=True)
def clear_store():
    store.reset()
    yield
    store.reset()
