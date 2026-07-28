#here we leran about ternury oper
#pb is if order vaule is above 300 0 rs below 300 cost 30 rs 

order_amount=int(input(f"enter the order amount :"))
#here user enter order amount user enter data bu input 
#we use int to convert give data
#in delivery we ternary opr insted of if else
# ternary oper|| value_if_true if condition else value_if_false 
delivery_fees = 0 if order_amount > 300 else 30

#here we will show the o/p based user given order amount 
print(f"delivery fees:{delivery_fees}")
#i added this 
total_amount = delivery_fees+order_amount
print(f"total amount of u r order is :{total_amount}")

