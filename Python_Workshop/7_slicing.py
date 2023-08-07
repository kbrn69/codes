#!/usr/bin/env python3

print("---------------Slicing is used in list, arrays and even in Conditional Statements-----------------")
asyn = "var[index] = value --> syntax to modify an index"
syn = "var[ start : stop-1 : step ] --> For lists and Conditional Statement"
print(asyn+"\n"+syn)


print("\nFew Examples are:")
x = "Hello World"
print(x[1:5])

l = [1,4,5,2,88,3,9,14,92]
     	
print(len(l)-1)
print(l[::])

# Defaults values for Start => 0'th index, Stop => len(var), step => 1

print("\n---------------------------------Deep copy/Shadow Copy---------------------------------------------")

list_one = [1, 3, 5, 7, 9, 11, 13, 14, 15]
m = list_one
print(list_one)
print(m)
print(id(list_one))
print(id(m))

#Both the values have the same ID here.

print("\n")

n = list_one.copy()
print(id(n))
print(id(list_one))

# copy() -> this method is used to copy an list into another variable with new ID

#another method of doing this without a function is by;

print("\n")
l = list_one[::1] # this is called deep copy
print(id(l))
print(id(list_one)) 
