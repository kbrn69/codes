 #!/usr/bin/env python3

print("---------------------------Address Comparision------------------------------")

print("since we know the purpose of id() and is keywords, we gonna see some examples")

# Case 1
print("CASE 1:  Let a = 10 and b = 10")
a = 10
b = 10

print(id(a))
print(id(b))
print("\n")

print("Let x and y are two lists")
x = [1,2,3,4]
y = [1,2,3,4]

print(id(x)) #Shows the ID i.e address of the variable.
print(id(y))

print(x is y) #compares the address of the variables.
print(y is x)

print(x == y) #compares the values present in the variables.
print(y == x)
print("\n")

# Case 2
print("""CASE 2: if the Id of one varible is the same Id of another variable,
then the elements modified in one variable will be reflected in the 
other variable""")

x = y # a = b is a assignment operator that assigns the same ID for both variables.
print(id(x))
print(id(y))

print(x.append(5)) # appending an element in one varible will cause the other to do the same
print(x)
print(y)

print(id(x)) #the Id will be same, therefore both var gets an element even if one is appended.
print(id(y))
print("\n")


print("""CASE 3: Any variable has a value above 256, will have differnt Id(Address)
for memory management""")

num_a = 280
num_b = 280
print(num_a is num_b)
print(id(num_a))
print(id(num_b))
print(num_a == num_b)
print(id(num_a) == id(num_b))
# this CASE 3 works only in interpreter, for no god known reason.
