
cup=input('chosen the cup size s/m/l:').lower()
print(f'this u r chosen size:{cup}')
#for s=5,m=10,l=20

if   cup == 's':
    print(f'price is 5')
elif cup == 'm':
    print(f'price is 10')
elif cup == 'l':
    print(f'price is 20')
else:
    print(f"chosen cup size is invalied ")