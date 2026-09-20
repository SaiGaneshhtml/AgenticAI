#optinal , mix , deep nesting model
from pydantic import BaseModel
from typing import Optional ,Union

#optional nested model

class Address(BaseModel):
    street: str
    city: str
    state: str
    zip_code: str

class Company(BaseModel):
    name: str
    address: Optional[Address] = None  # Optional nested model

class User(BaseModel):
    name: str
    email: str
    company: Optional[Company] = None  # Optional nested model

#mix nested model here we use uinion 

class Textcontent(BaseModel):
    text: str
    content_type: str

class Imagecontent(BaseModel):
    url: str
    content_type: str

class article(BaseModel):
    title: str
    content: Optional[Union[Textcontent, Imagecontent]] = None  # Union of nested models


# deeply 

class Country(BaseModel):
    code: str
    name: str

class State(BaseModel):
    name: str
    country:Country

class City(BaseModel):
    name:str
    state:State

class Adress(BaseModel):
    stree:str
    pin_code:str
    city:City


