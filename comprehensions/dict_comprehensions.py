# here we know how user comprehetion with key pair works in python

chai_ind={
    'masala chai': 200,
    'ginger chai': 150,
    'lemon chai': 100,
    'green tea': 2500,
    'lemon chai': 100,
    'masala chai': 2000
}
# this    {key: value / x    for  key , vaule in dictionary.items()
#  iteam is method which help garb both key and pair}  
# is the syntax for user comprehension with key pair
chai_usd= { tea: price / 95 for tea, price in chai_ind.items() }

print(chai_usd)