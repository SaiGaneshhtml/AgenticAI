#use if else to make sure get the o/p for user 
snack= input('enter u r perfer snack:').lower()
#with the lower if user enter case sensitive also we will not effect 
print(f'u r order conformation:{snack}')
if snack=='puff' or snack=='samosa':
    print(f'we have ;){snack}')
else:
    print(f'we sorry :(')