def name():
    yield "Alice"
    yield "Bob"
    yield "Charlie"

st_names = name()
print(next(st_names))  # Output: Alice
print(next(st_names))  # Output: Bob
print(next(st_names))  # Output: Charlie

#normal 

def name_one():
    return ["Alice", "Bob", "Charlie"]

print(f"this form the normal function: {name_one()}")

# return = "Give me everything now."
# yield = "Give me one item now, and I'll ask for the next one later."

# A generator is a special function that uses yield to produce one value at a time instead of returning all values at once.
# It saves memory and is ideal for processing large datasets or streams of