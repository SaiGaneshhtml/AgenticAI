# here we learn how to handly the error 

coffee = {"black": 55, "tea": 100}

user_order = "milk"  # simulate user input

try:
    value = coffee[user_order]
except KeyError:
    print(f"Sorry, '{user_order}' is not available")
else:
    print(f"Order placed! {user_order} coffee = ₹{value}")

