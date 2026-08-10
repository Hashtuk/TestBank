import json
from typing import Optional

import allure
import requests
from requests import Response

from Module_5.src.main.api.configs.config import Config
from Module_5.src.main.api.foundation.http_requester import HttpRequester
from Module_5.src.main.api.models.base_model import BaseModel


SENSITIVE_FIELDS = {'authorization', 'password', 'token'}


def _mask_sensitive_fields(payload):
    if isinstance(payload, dict):
        return {
            key: '***' if key.lower() in SENSITIVE_FIELDS else _mask_sensitive_fields(value)
            for key, value in payload.items()
        }
    if isinstance(payload, list):
        return [_mask_sensitive_fields(value) for value in payload]
    return payload


def _allure_payload(payload) -> str:
    return json.dumps(_mask_sensitive_fields(payload), ensure_ascii=False, default=str)


class CrudRequester(HttpRequester):
    def post(self, model: Optional[BaseModel] = None) -> Response:
        body = model.model_dump() if model is not None else ''

        with allure.step(f'post {Config.fetch("backendUrl")}/{self.endpoint.value.url}'):
            allure.attach(_allure_payload(body), 'Request body', allure.attachment_type.JSON)

        response = requests.post(
            url=f'{Config.fetch("backendUrl")}/{self.endpoint.value.url}',
            headers=self.request_spec,
            json=body
        )

        try:
            response_body = response.json()
        except requests.JSONDecodeError:
            response_body = response.text
        allure.attach(_allure_payload(response_body), 'Response body', allure.attachment_type.JSON)
        self.response_spec(response)
        return response

    def delete(self, user_id: int) -> Response:
        response = requests.delete(
            url=f'{Config.fetch("backendUrl")}/{self.endpoint.value.url}/{user_id}',
            headers=self.request_spec
        )
        self.response_spec(response)
        return response
