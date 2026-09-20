from typing import List, Optional, Dict
from pydantic import BaseModel , field
import re  #needed for regex validation , reguler expression

class ClassA(BaseModel):
    id: int
    name: str = field (
        ...,# Required field with a description
        min_length=4,
        max_length=50,
        description="use char from 4 to 50",
        example="bill" 
    )  # Required field with a description

    salary: float = field(
        ...,# Required field with a description
        gt=10000,  # Greater than 0
        le=100000,  # Less than or equal to 100000
        description="Salary must be greater than 0"
    )  # Required field with a description

    phone_number: str = field(
        ...,# Required field with a description 
        regex=r'^\+?\d{10,15}$',  # Regex pattern for phone number validation
        description="Phone number must be a valid format (e.g., +1234567890)"
    )  # Required field with a description


