from pydantic import BaseModel

class Address(BaseModel):
    street: str
    city: str
    state: str
    zip_code: str   


class User(BaseModel):
    name: str
    email: str
    address: Address  # Nested model


#object creation with nested model

user_data = {
    "name": "John Doe",  
    "email": "john.doe@example.com",
    "address": {
        "street": "123 Main St",
        "city": "Anytown",
        "state": "CA",
        "zip_code": "12345"
    }
}

user_data_1 = {
    "name": "kill bill",       
    "email": "kill.bill@gmail.com",
    "address": {
        "street": "456 Oak Ave",
        "city": "Somewhere",
        "state": "NY",
        "zip_code": "67890usde"
    }
}
user = User(**user_data) 
user_1 = User(**user_data_1)  # Create a User instance with nested Address model
print(user)
print(user_1)