#string 
#core
#indexing 
#slicing
#theser are topic i will leran


bank_name = "HDFCBank"
person_name = "raw"

print(f"the bank{bank_name} gave loan to this person name is {person_name}")
#indexing 
print(f"the first letter of bank name is {bank_name[0]}") #H
print(f"the last letter of bank name is {bank_name[4]}") #c here is c is inclusive
#here in py the [start :end ]will follow 

#here we can also show 
print(f"the bank name is {bank_name[::-3]}") #-3 is step value here it will
#print the bank name in reverse order
#like kbd
print(f"the substring of bank name is {bank_name[:4]}") #HDFC
print(f"the substring of bank name is {bank_name[5:]}") #Bank
#encode and decodeed way of sting 
lable='విద్యార్థి'
encoded_lable=lable.encode('utf-8')
print(f"the encoded lable is {encoded_lable}") #b'\xff\xfe\x00\x00'
decoded_lable=encoded_lable.decode('utf-8')
print(f"the decoded lable is {decoded_lable}") #విద్యార్థి