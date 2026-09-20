from pydantic import BaseModel,model_validator, field_validator
from datetime import datetime
# field validator  

class ClassA(BaseModel):
     first_name: str
     last_name: str

     @field_validator('first_name', 'last_name')
     def capital_name(cls, v):
       if v != v.capitalize():
         raise ValueError('Name must be capitalized')
       return v

class Money(BaseModel):
    amount: str 

    @field_validator('amount' , mode='after')  
    def validate_amount(cls, v):
         if isinstance(v, str):
              return v.replace('$', '')  # Remove commas and dollar signs from the string
         return v

class DateandTimeModel(BaseModel):
    start_time: datetime
    end_time: datetime

    @model_validator(mode='after')
    def validate_time(cls, values):
        if values.start_time >= values.end_time:
            raise ValueError('Start time must be before end time')
        return values