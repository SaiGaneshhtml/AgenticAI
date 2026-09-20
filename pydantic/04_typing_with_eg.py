from pydantic import BaseModel
from typing import List, Optional,Dict 

class ClassA(BaseModel):
    id: int
    name: str
    tags: List[str] 
     # A list of strings
    metadata: Optional[Dict[str, str]] = None  
    # An optional dictionary with string keys and values

input_data = {
    'id': 1,
    'name': 'Example',
    'tags': ['tag1', 'tag2'],
    'metadata': {'key1': 'value1', 'key2': 'value2'}
}
product = ClassA(**input_data)
print(product)