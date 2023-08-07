#!/usr/bin/env python3


print("--------------------------------------------CURD--------------------------------------------------")
print("C -> Create,\nU -> Update,\nR -> Read,\nD -> Delete")
print("The CURD operation is important and should be mastered")
print("\n")
alpha = input("Enter a String: ")

beta = int(input("Enter an Integer: "))

print("To get Input from user in CLI ----> input()")
print("To get Length of an variable -----> len()")

print(f"Your Word is {alpha}")
print(f"The length of the given word is {len(alpha)}")

print("Your Given Number is {}".format(beta))

x = [13, "Vada", "nonna", 69]
print("To join a element/item/variable at the end of an list --> append()")
print(x.append(alpha))

print("To remove the last item in the list and returns --> var.pop()")
print("To remove an item in any value, it deletes its first occurance --> remove()")
print("To delete an item using position, used for lists, strings ----> del var[index]")

