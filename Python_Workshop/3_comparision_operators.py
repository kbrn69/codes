#!/usr/bin/env python3

print("----------------------Comparision Operators-----------------------")

print("== Equality")
print("!= InEquality")
print("> GreaterThan")
print("< LesserThan")
print(">= GreaterThan Or Equalto")
print("<= LesserThan or Equalto")


print("""
All the Comparision Operations compares only the values in 
the variable gives Boolean Value i.e True or False""")
print("\n")
print("-----------------------------Boolean----------------------------")
print(" 1 => True ")
print(" 0 => False ")

print("\n")
print("-----------------------Chaining Comparision--------------------")
print("Two or more comparition operators can be done by LogicalGates")
print(" AND ")
print("0 & 0 = 0")
print("0 & 1 = 0")
print("1 & 0 = 0")
print("1 & 1 = 1")

print("\n")
print(" OR ")
print("0 || 0 = 0")
print("0 || 1 = 1")
print("1 || 0 = 1")
print("1 || 1 = 1")

print("\n")
print(" NOT ")
print(" ^1 = 0 ")
print(" ^0 = 1 ")

print("\n")
print("--------------------------Address Comparision---------------------")
print(" id() => gives the address of a Variable")
print(" is => compares two variable's ID and gives output in Boolean")
print("\n")

x = 15
y = 66
print(id(x))
print(id(y))

print(x is y)
print(y is x)

a=10
b=10
print(a is b)
print(b is a)


