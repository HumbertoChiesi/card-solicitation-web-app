from pydantic import BaseModel, Field, validator, constr

from datetime import datetime

from validate_docbr import CPF


class CreditCardApplication(BaseModel):
    name: str
    age: int
    sex: str
    address: str
    phone_number: int
    CEP: str
    CPF: str
    income: float
    credit: float
    created_on: datetime = Field(default_factory=datetime.now)

    @validator('income')
    def validate_income(cls, value):
        if value <= 1.212:
            raise ValueError("Your income should be at least 1 minimum wage")
        return value

    @validator('age')
    def validate_age(cls, value):
        if value >= 100 or value < 18:
            raise ValueError("You cant be younger than 18 years old or older than 100 years old")
        return value

    @validator('CPF')
    def validate_cpf(cls, value):
        cpf_val = CPF()
        if not cpf_val.validate(value):
            raise ValueError("The CPF is wrong!")
        return value
