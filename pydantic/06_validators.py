from pydantic import BaseModel , validator ,model_validator ,field_validator
from typing import List, Optional,Dict

class ClassA(BaseModel):
    username: str

    @field_validator('username')
    def validate_username(cls, v):
        if len(v) < 3:
            raise ValueError('Username must be at least 3 characters long')
        return v

class ClassB(BaseModel):
    password: str
    confirm_password: str 


    @model_validator(mode='after') # after mode will perform validation after the model fields have been initialized.
    def validate_password(cls, values):
        if values.password != values.confirm_password:
            raise ValueError('Passwords do not match')
        return values

    #                 ClassB(BaseModel)
    #                    │
    #                    ▼
    #       ┌─────────────────────────┐
    #       │ Receive input data      │
    #       │                         │
    #       │ password="123"          │
    #       │ confirm_password="123"  │
    #       └────────────┬────────────┘
    #                    │
    #                    ▼
    #       ┌─────────────────────────┐
    #       │   Pydantic BaseModel    │
    #       │   validates fields      │
    #       └────────────┬────────────┘
    #                    │
    #             ┌──────┴──────┐
    #             ▼             ▼
    #     password: str   confirm_password: str
    #             │             │
    #             └──────┬──────┘
    #                    ▼
    #       ┌─────────────────────────┐
    #       │ ClassB model initialized│
    #       │                         │
    #       │ values.password         │
    #       │ values.confirm_password│
    #       │        available        │
    #       └────────────┬────────────┘
    #                    │
    #                    ▼
    #    @model_validator(mode='after')
    #                    │
    #                    ▼
    #       ┌─────────────────────────┐
    #       │ validate_password()     │
    #       │                         │
    #       │ password ==             │
    #       │ confirm_password ?      │
    #       └────────────┬────────────┘
    #                    │
    #           ┌────────┴────────┐
    #           │                 │
    #          YES                NO
    #           │                 │
    #           ▼                 ▼
    #     return values     ValidationError
    #           │                 │
    #           ▼                 ▼
    #     Valid ClassB        ❌ Error