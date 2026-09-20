from pydantic import BaseModel

class Product(BaseModel):
    id: int
    name: str
    price: float 
    offer: bool = False  # Default value for the 'offer' field

    # TypeScript:  offer?: boolean     → optional field
    # Pydantic:    offer: bool = False → optional + default value

product = Product(id=1, name="Laptop", price=999.99 , offer=True)  # Creating an instance of the Product model
product_1 = Product(id=2, name="Smartphone", price=599.99)
product_2 = Product(name="Tablet")  

print(product)