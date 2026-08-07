def cup():
    n=1
    while True:
        yield n
        n += 1  

n=cup()
x=cup()
# if we no need user var we can use  _
for _ in range(5):  
    print(next(n))

for _ in range(4):  
    print(next(x))