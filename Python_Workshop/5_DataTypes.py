#!/usr/bin/env python3

print("-------------------------------Data Types------------------------------------")
print("""Knowing about Mutable and Immutable in datatypes is an important thing,
MUTABLE = Data can be modified, Id(Address) will be same.
IMMUTABLE = Data can't be modified , if modified Id(Address) will be changed.
""")

print("""Integer => Immutable
Float  => Immutable
String => Immutable
List  => Mutable
Tuple => Immutable  
Dict  =>
Set   =>
""")
print("type() --> This datatype is used to identify the type of datatype")

print("----------------------------------Integer----------------------------------")
x = 1
y = -33
print(type(x))
print(type(y))



print("-----------------------------------Float----------------------------------")
w = 82.9
x = -20.0
print(type(w))
print(type(x))




print("-----------------------------------String--------------------------------")

name = "alpha user"
print(id(name))
lastname = "alpha user"
print(id(lastname))
#Above variables has the same string, yet they differ in python interpreter.
#but if the string has the qualities of an Identifies, its address will be same. 

word = "Vannakam Chennai"
print(word[4]) # [] => indicates indexing of string, and it starts from 0.
print(word[-1]) # -1 starts from backwards.

print("\nFormating in string :")
print("Formating String by using {} and 'format' keyword")

name = "Bruce Wayne"
print("Welcome, Mr.{}".format(name)) # 1st type of formating
print(f"Welcome, Mr.{name}")         # 2nd type of formating

print("\nConcatination of String :")
p = "hello"
q ="World"
print(p + q)



print("---------------------------------List-------------------------------------")

print("Known as collection of characters, variables, datatypes and even another List")
print("[ ] Square brackets are used to indicate List, They are Mutable")

list_x=[1,2,"Hello","world"]
print(list_x)

print("\nList keyword to create list/typecast -> list() ")

print("\nIndexing is accessing elements my impling a number(position) in [ ] by default elements starts with 0, where -1 starts from last element.")
print(list_x[3])
print("Indexing Concept also applicable for String")  

print("\n")




print("---------------------------------Tuples-------------------------------------")
print("\n")

print("Tuple can be implemented using its funtion called -> tuple()")
print("\nTuples are Basically List, but Tuples are Immutable")
tup = tuple() # creating a empty tuple, method 1.
t = ()
print(type(tup))
print(type(t)) 

print("Tuple packing and unpacking")

tone, ttwo, tthree = (1, 3, 8) # the variables takes the value in each index, "Type 1"
print(tone)
print(ttwo)
print(tthree)

# if the tuple has more values it can be assigned with astrisk '*' in front of the variable, "Type 2":
tup_two = (12, 13, 14, 15, 16, 22, 33, 77, 99, 69)
*pp, qq, zz = tup_two # the Output will results as a List
print(pp)
print(qq)
print(zz)

print("Swaping of Two Variables, without temporary Variable")
love = 99
hate = 1
print(f"value of love is {love} and hate is {hate}")
love, hate = (hate, love)  # The values are getting swapped and get assigned accorrding to their position
print(f"Value of love is {love} and hate is {hate}")


print("\n")
print("--------------------------------Dictonary------------------------------------")
print("\n")

print("Dictonary is collection of data, with key-value pair, Creating a empty Dictonary: ")
dictx = {} #using parenthesis
dicty = dict() #using functions
print(type(dictx))
print(type(dicty))


print("""\n Its syntax is :
		x = { "key" : "value" }
	""")
# Key should be an Immutable datatype, eg: Int, Float, String, Bool, Tuple

dict_x = { "a" : 1, "b" : 2, "c" : 3, "d" : 4 }
print(dict_x) 

print(dict_x["b"]) # within the squarebracket the key should be called upon.
 
# "in" -> this keywprd is used to check the element present inside a dict

print("a" in dict_x)


# Dict Packing and Unpacking:

dict_items = { 1 : "onnu", 2 : "rendu", 3 : "moonu", 4 : "naalu", 5 : "aanji"}
print(dict_items)
a, b, c, d, c = dict_items
print(a) # only the keys gets copied.

# Adding Items to the Dict:

dict_a = { 1 : "a", 2 : "b", 3 : "t" }
dict_b = { 4 : "f", 5 : "l" }

dict_a = { **dict_b } # This syntax replaces the values of the variable with the '**' variables.
print(dict_a) 


print("\n")
print("----------------------------------set-----------------------------------------------")
print("\n")

print("Set is a value less dictionary, which results in no duplicate items.")

set_x = set() #Creates an empty set.
print(type(set_x))

print("Values inside a Set should be Immutable datatype.")

set_x = {1, 1, 2, 2, 3, 3}
print(set_x) #Output doesn't gives duplicate values.





















