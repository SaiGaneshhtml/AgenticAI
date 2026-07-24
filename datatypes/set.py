#set
set_a={1, 2, 3, 4, 5}
set_b={4, 5, 6, 7, 8}

set_c= set_a|set_b #join
print(f"the union of two set is {set_c}")#union of two set
set_d= set_a&set_b #common
print(f"the intersection of two set is {set_d}")#intersection of two set
set_e= set_a-set_b# difference
print(f"the difference of two set is {set_e}")#difference of two set
#membership test 
#check the given element is present in the set or not "in" operator
print(f"the 3 is in set_a? {3 in set_a}")#true
print(f"the 9 is in set_a? {9 in set_a}")#false