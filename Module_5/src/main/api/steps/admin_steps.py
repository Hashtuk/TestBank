from Module_5.src.main.api.configs.config import Config
from Module_5.src.main.api.foundation.endpoint import Endpoint
from Module_5.src.main.api.foundation.requesters.crud_requester import CrudRequester
from Module_5.src.main.api.foundation.requesters.validated_crud_requester import ValidatedCrudRequester
from Module_5.src.main.api.models.create_credit_user_request import CreateCreditUserRequest
from Module_5.src.main.api.models.create_user_request import CreateUserRequest
from Module_5.src.main.api.models.login_user_request import LoginUserRequest
from Module_5.src.main.api.steps.base_steps import BaseSteps
from Module_5.src.main.api.specs.request_specs import RequestSpecs
from Module_5.src.main.api.specs.response_specs import ResponseSpecs


class AdminSteps(BaseSteps):
    @staticmethod
    def _admin_headers():
        return RequestSpecs.auth_headers(
            username=Config.fetch('adminUsername'),
            password=Config.fetch('adminPassword')
        )

    def create_user(self, create_user_request: CreateUserRequest | CreateCreditUserRequest):
        response = ValidatedCrudRequester(
            request_spec=self._admin_headers(),
            endpoint=Endpoint.ADMIN_CREATE_USER,
            response_spec=ResponseSpecs.request_ok()
        ).post(create_user_request)

        self.created_obj.append(response)
        return response

    def create_user_invalid(self, create_user_request: CreateUserRequest,
                            expected_res: ResponseSpecs):
        return CrudRequester(
            request_spec=self._admin_headers(),
            endpoint=Endpoint.ADMIN_CREATE_USER,
            response_spec=expected_res
        ).post(create_user_request)

    def delete_user(self, user_id: int):
        response = CrudRequester(
            request_spec=self._admin_headers(),
            endpoint=Endpoint.ADMIN_DELETE_USER,
            response_spec=ResponseSpecs.request_ok()
        ).delete(user_id)
        self.created_obj[:] = [
            obj for obj in self.created_obj
            if getattr(obj, 'id', None) != user_id
        ]
        return response

    def login_user(self, login_user_request: LoginUserRequest):
        response = ValidatedCrudRequester(
            request_spec=RequestSpecs.unauth_headers(),
            endpoint=Endpoint.LOGIN_USER,
            response_spec=ResponseSpecs.request_ok()
        ).post(login_user_request)
        return response
