
# Variables and data types
# Variables store data. Python has these basic types:

# Integers: age = 25
# Floats: price = 19.99
# Strings: name = "Alice"
# Booleans: is_student = True

#Example:
# name = "Alice"
# age = 30
# print("Name:", name)
# print("Age:", age)



#Use input to get data from user
# user_name = input("Enter your name: ")
# print("Hello,", user_name)




#Basic arithmetic operations
# a = 10
# b = 3
# print(a + b)  # 13 (addition)
# print(a // b) # 3 (integer division)
# print(a ** 2) # 100 (exponent)




#strings concatenation:
# greeting = "Hello " + "World!"
# print(greeting)  # "Hello World!"

#Comparison:
# print(5 > 3)  # True
# print(5 == 3) # False




#control flow
# if-else statement


# age = 10
# if age >= 18:
#     print("You are an adult.")
# else:
#     print("You are a minor.")   



# # for loop
# for i in range(5):
#     print(i)  # prints numbers from 0 to 4


# while loop
# count = 0
# while count < 5:
#     print("looping!")
#     count += 1  # increment count by 1




#Functions

# def my_function(a, b):
#     return a + b
# result = my_function(5, 3)
# print(result)  # prints 8



# def greet(first_name, last_name):
#     return f"Hello, {first_name} {last_name}!"
# fullname = greet(  first_name="Alice", last_name="Smith")
# print(fullname)  # prints "Hello, Alice Smith!"






#Lists (arrays)

# fruits = ["apple", "banana", "cherry"]
# print(fruits[0])  # prints "apple"


#store multiple items in a list

# numbers = [1, 2, 3, 4, 5]
# print(numbers)  # prints [1, 2, 3, 4, 5]
# numbers.append(6)  # add 6 to the list
# print(numbers)  # prints [1, 2, 3, 4, 5, 6]








#simple calculator

# num1 = int(input("Enter first number: "))  # you can use float() for decimal numbers
# num2 = int(input("Enter second number: "))    
# result = num1 + num2
# print("The sum is:", result)  # prints the sum of num1 and num2








#type conversion

# Convert string to integer
# age_str = "25"
# age_int = int(age_str)
# print(age_int)  # 25
# print(type(age_int))  # <class 'int'>

# # Convert float to integer (truncates decimals)
# pi = 3.14
# print(int(pi))  # 3

# # Convert to string
# price = 9.99
# print("Price: $" + str(price))




#defining functions

# def name_of_function(name):
#     print("Hello, " + name + "!")

# name_of_function("Alice")  #calls the function with "Alice" as an argument


# def add_numbers(a, b):
#     print("The sum is:", a + b)
# add_numbers(5, 5)  # prints "The sum is: 15"







# def is_even(number):

#     if number % 2 == 0:
#         return True
#     elif number % 2 == 1:
#         return False
# print(is_even(4))  #print true when number is even and false when number is odd








#loop control

# for i in range (10):
#     if i == 2:
#         continue
#     if i == 9:
#         break

#     print(i) # prints numbers from 0 to 9, skipping 2 and stopping at 9

