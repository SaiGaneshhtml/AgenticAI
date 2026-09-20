from pydantic import BaseModel
from typing import List, Optional,Dict 

class ClassA(BaseModel):
    id: int
    name: str
    tags: List[str] 
     # A list of strings
    metadata: Optional[Dict[str, str]] = None  
    # An optional dictionary with string keys and values


    #          here we taking str form pydentic and
    #  we are using List and Dict from typing   module to
    #  define the types of the fields in the ClassA model.
    # 
    #  The 'tags' field is a list of strings, and the 'metadata' field is an optional dictionary 
    # with string keys and values. If 'metadata' is not provided, it will default to None.