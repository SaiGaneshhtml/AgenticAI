#operator over laoding 
ind=["100","3000","200","300" ]
usd=["100"]
print(f"the addition of two list is {ind+usd}")#addition of two list
print(f"the multiplication of two list is {ind*3}")#multiplication of list


#bytearray
# here each element of the bytearray is a integer in the range 0<=x<256
#each ele treat as a arr
byte_array=bytearray(b"[1,2,3,4,5]")
byte_array=byte_array.replace(b"2",b"22")#[1,22,3,4,5]

print(f"the byte array is {byte_array}")

