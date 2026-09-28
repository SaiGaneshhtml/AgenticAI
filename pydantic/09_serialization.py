# here we can go thought with how to use convetion,dict,json str
from pydantic import BaseModel , ConfigDict  # config 
from datetime import datetime
from typing import List 
 

class Adress(BaseModel):
   stree : str
   pin_code : int

   model_config = ConfigDict(
       json_encode={datetime : lambda v:v.strftime('%d-%m-%Y')}
    )

class User (BaseModel):
   name : str
   email : str
   address : Adress
   creat_id: datetime
   

user = User(
   name = 'sai',
   email = 'sai@ai',
   address = Adress(
     stree = 'hyd',
     pin_code = '101020'
    ),

   creat_id= datetime(2026,4,7)
   
)


use_dict = user.model_dump()
print(user)
print('='*15)
print(use_dict)


use_dict2 = user.model_dump_json()
print(user)
print('='*15)
print(use_dict2)