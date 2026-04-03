from typing import Annotated

from Module_5.src.main.api.generators.rule_creation import RuleCreation
from Module_5.src.main.api.models.base_model import BaseModel


class CreateCreditUserRequest(BaseModel):
    username: Annotated[str, RuleCreation(regex=r'^[A-Za-z0-9]{3,15}$')]
    password: Annotated[str, RuleCreation(regex=r'^[A-Z]{3}[a-z]{1}[0-9]{2}[!$_]{4}$')]
    role: Annotated[str, RuleCreation(regex=r'^ROLE_CREDIT_SECRET')]