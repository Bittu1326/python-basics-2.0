# #ERROR HANDLING:
# #-> Errors are mistakes in a program that stop it from working correctly.
# #-> Exceptions is a special type of error that occurs while the program is running.
# #-> Python provides ways to handle exceptions so that the program doesn't crash suddenly.
# #Types of Errors:
# #1.Compile time Error(Syntax error)
# #   Errors that happen when the code is not written correctly(wrong syntax )     
# #2.Logical Error
# #   Errors when the program runs but gives wrong output because the logic is wrong.
# #3.Runtime Error  (Exceptions)
# #   Errors happens when the program is running.

# # TYPES OF EXCEPTIONS IN PYTHON:

# #1. ZeroDivisionError:
# #2. ValueError:
# #3. IndexError:
# #4. KeyError:
# #5. TypeError:
# #6. NameError:
# #7. FileNotFoundError:


# #1. Zero Division Error:    It is an exception which divides a number by zero.

# try:
#     a=int(input("enter the numerator:"))
#     b=int(input("enter the denominator:"))
#     c=a/b
#     print(c)
# except ZeroDivisionError:
#     print("Error: Division by zero is not possible")

# try:
#     i=2
#     n=int(input("Enter a value: "))
#     if i%n==0:
#         print("even")
#     else:
#         print("Odd")
# except ZeroDivisionError:
#     print("Error: Division by zero is not possible")

# try:
#     i=3
#     n=int(input("Enter a value: "))      #0
#     if i%n==0:
#         print("Yes, number is a multiple of",n)
#     else:
#         print("No, number is not multiple of",n)
# except ZeroDivisionError:
#     print("Error: Division by zero is not possible")

# #2. Value Error:    It's an Exception that gives as invalid value given.

# try:
#     rollno=int(input("Enter the roll no: "))
#     print(rollno)
# except ValueError:
#     print("Error: Given is not in the integer datatype")

# #3. IndexError:

# list=["bot","lucky","bittu","bhai"]
# print(list)

# try:
#     print(list[4])
# except IndexError:
#     print("Error: Index is out of range for list")

# my_string="bot"
# print(my_string)

# try:
#     print(my_string[-4])
# except IndexError:
#     print("Error: negative index is out of range")

#  #4. KeyError:

# dict={"Name":"Bhai","kaam":"Web Developer"}
# print(dict)
# try:
#     value=dict["game"]
# except:
#     print("The key 'game' doesnt exist in the dict")

# #5. TypeError:
# try:
#     List=[10,20,30]
#     sum=List+5
#     print(sum)
# except TypeError:
#     print("Invalid type operation")

# #6. NameError:
# try:
#     print(mult)
# except NameError:
#     print("variable not declared")

#7. FileNotFoundError:

