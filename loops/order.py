# here we leran about continu and brack 

drinks = ['tea','out of stock','coffee','discontinuce','water']

for name in drinks:
    if name == 'out of stock':
        # print(f"{name}out of stock")
        continue # here loop will skip the give name 
    if name == 'discontinuce':
        break #here loop will enf 
    print(f"{name} : iteam found")
print(f"these are avali")





# people = [(11, 'shannu'), (33, 'sree'), (22, 'gun')]

# for age, name in people:
#     if age >= 18:
#         print(f"{name} is ready to work")
#         break
# else:
#     print("No one is ready to work")
