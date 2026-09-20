
from pydantic import BaseModel, computed_field ,Field

class MyModel(BaseModel):
    a: int
    b: int

    @computed_field
    @property
    def sum(self) -> int:
        return self.a + self.b

class Room_booking(BaseModel):
    room_id: int
    nights: int = Field(... ,ge=1)  # Default to 1 night, must be at least 1

    @computed_field
    @property
    def total_cost(self) -> float:
        # Assuming a fixed cost per night for simplicity
        cost_per_night = 100.0
        return self.nights * cost_per_night

booking = Room_booking(room_id=101, nights=3)
print(f"Total cost for booking: ${booking.total_cost}")  # Output: Total cost for booking: $300.0
    