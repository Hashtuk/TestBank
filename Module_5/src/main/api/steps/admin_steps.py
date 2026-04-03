from Module_5.src.main.api.foundation.endpoint import Endpoint
from Module_5.src.main.api.foundation.requesters.crud_requester import CrudRequester
from Module_5.src.main.api.foundation.requesters.validated_crud_requester import ValidatedCrudRequester
from Module_5.src.main.api.models.create_user_request import CreateUserRequest
from Module_5.src.main.api.models.login_user_request import LoginUserRequest
from Module_5.src.main.api.steps.base_steps import BaseSteps
from Module_5.src.main.api.specs.request_specs import RequestSpecs
from Module_5.src.main.api.specs.response_specs import ResponseSpecs


class AdminSteps(BaseSteps):
    def create_user(self, create_user_request: CreateUserRequest):
        response = ValidatedCrudRequester(
            request_spec=RequestSpecs.auth_headers(username='admin', password='123456'),
            endpoint=Endpoint.ADMIN_CREATE_USER,
            response_spec=ResponseSpecs.request_ok()
        ).post(create_user_request)

        self.created_obj.append(response)
        return response

    def delete_user(self, user_id: int):
        CrudRequester(
            request_spec=RequestSpecs.auth_headers(username='admin', password='123456'),
            endpoint=Endpoint.ADMIN_DELETE_USER,
            response_spec=ResponseSpecs.request_ok()
        ).delete(user_id)

    def login_user(self, login_user_request: LoginUserRequest):
        response = ValidatedCrudRequester(
            request_spec=RequestSpecs.unauth_headers(),
            endpoint=Endpoint.LOGIN_USER,
            response_spec=ResponseSpecs.request_ok()
        ).post(login_user_request)
        return response