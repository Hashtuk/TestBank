from Module_5.src.main.api.configs.config import Config
from Module_5.src.main.api.foundation.http_requester import HttpRequester
from Module_5.src.main.api.foundation.requesters.crud_requester import CrudRequester
from Module_5.src.main.api.models.base_model import BaseModel
import allure


class ValidatedCrudRequester(HttpRequester):
    def __init__(self, request_spec, endpoint, response_spec):
        super().__init__(request_spec, endpoint, response_spec)
        self.crud_requester = CrudRequester(
            request_spec=request_spec,
            endpoint=endpoint,
            response_spec=response_spec
        )

    def post(self, model: BaseModel | None = None) -> BaseModel:
        response = self.crud_requester.post(model)
        with allure.step(f'post {Config.fetch('backendUrl')}/{self.endpoint.value.url} and validated model'):
            allure.attach(f'Validated model response: {self.endpoint.value.response_model.__name__}',
                          'Validated model',
                          allure.attachment_type.TEXT)
        self.response_spec(response)
        return self.endpoint.value.response_model.model_validate(response.json())

    def delete(self, user_id: int):
        response = self.crud_requester.delete(user_id)
        self.response_spec(response)
        return self.endpoint.value.response_model.model_validate(response.json())

# class ValidatedCrudRequester(CrudRequester):
#     def post(self, model: BaseModel) -> BaseModel:
#         response = super().post(model)
#         self.response_spec(response)
#         return self.endpoint.value.response_model.model_validate(response.json())