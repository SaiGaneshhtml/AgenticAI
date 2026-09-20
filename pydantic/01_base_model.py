from pydantic import BaseModel
#r current understanding, use this bottom line:

# Pydantic takes the input for each field, tries to validate/convert
#   it into the type you declared
#    for that field, and raises ValidationError if it can't satisfy that type.
class User(BaseModel):
    id: int
    name: str
    signup_ts:bool

input_data = {'id': 123, 'name': '321', 'signup_ts': True}
user = User(**input_data)
# "**"" unpacked the dictionary into keyword arguments for the User model

print(user)
