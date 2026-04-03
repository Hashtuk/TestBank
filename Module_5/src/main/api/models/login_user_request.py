from Module_5.src.main.api.models.base_model import BaseModel


class LoginUserRequest(BaseModel):
    username: str
    password: str