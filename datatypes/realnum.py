#real num
import sys  
from decimal import Decimal as GUN #thsi we call as type casting where
#we are changing the data type of the variable
ideal_val=4.8
real_val=99.9999

print("ideal value is",ideal_val)
print("real value is",real_val)
print("difference between ideal and real value is",real_val-ideal_val)
#we need use packages 
print(sys.float_info) #this will give us the float info of the system

print(GUN(real_val))#here GUN is used to convert the float value to decimal value