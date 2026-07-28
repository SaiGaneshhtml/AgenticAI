device_status= 'active'
#temp= input(f'enter the temp num')
temp = float(input("Enter the temperature: "))

if device_status == 'active':
    if temp > 35:
        print(f'high')
    else:
        print("normal.")
else:
    print(f'deactive offline')