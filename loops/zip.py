#here we learn about zip
#zip help iterart 2 obj 

person = ['sai','shannu','sree']
bill   = [22,44,55]

for name,amount in zip(person , bill):
    print(f"{name} pay : {amount}")