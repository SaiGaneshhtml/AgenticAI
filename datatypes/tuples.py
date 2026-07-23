#tuples
dosa_type=("masale","onion","tomato","chilli")

(type1,type2,type3,type4)=dosa_type
print(f"the dosa type is {dosa_type}")
#here in tuples type1,type2,type3,type4 are unpacking the values of tuple dosa_type
#tuples are immutable we cannot change the values of tuple once it is created

onion_dosa,tomato_dosa=1,3
print(f"the dosa o:{onion_dosa}and t:{tomato_dosa}")
tomato_dosa,onion_dosa= tomato_dosa,onion_dosa
print(f"the dosa t:{tomato_dosa}and o:{onion_dosa}")
#with the above code we can swap the values of two variables without using third variable
#member ship test
print(f"the ragi dosa is in dosa_type? {'ragi' in dosa_type}")#fales 
#here with in the tuple chekc give on is there o not for ragi it show false
print(f"the masale dosa is in dosa_type? {'masale' in dosa_type}")#true
