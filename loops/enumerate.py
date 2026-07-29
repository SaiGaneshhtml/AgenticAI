#here we learn about enumart
#why we use to num the iteam with help of inde and we can custmize the numbering  the lis 

arr = ['coffee','tea','colldrink','water']

for index , drinks in enumerate (arr , start=2):
    print(f"num of drinks:{index}::{drinks}")