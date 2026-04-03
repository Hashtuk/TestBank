import pytest

from Module_5.src.main.api.classes.api_manager import ApiManager


@pytest.fixture
def api_manager(created_obj):
    return ApiManager(created_obj)