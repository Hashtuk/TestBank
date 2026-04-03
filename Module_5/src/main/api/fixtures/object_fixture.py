import logging

import pytest
from typing import List, Any

from Module_5.src.main.api.classes.api_manager import ApiManager
from Module_5.src.main.api.models.create_user_response import CreateUserResponse


@pytest.fixture
def created_obj():
    objects: List[Any] = []
    yield objects
    clean_user(objects)


def clean_user(objects: List[Any]):
    api_manager = ApiManager(objects)
    for o in objects:
        if isinstance(o, CreateUserResponse):
            api_manager.admin_steps.delete_user(o.id)
        else:
            logging.warning(f'Failed to delete user_id: {o.id}')