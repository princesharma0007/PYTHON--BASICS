# try:
#     a = int(input())
#     b = int(input())
#     print(a/b)

# # except:
# #     print("ERROR"). #manual error

# # except ZeroDivisionError:
# #     print("cannot divide my zero") #using class zerodivisson class

# except ZeroDivisionError as e:
#     print(e)

# except ValueError as f:
#     print(f)

# age = int(input("Enter your age: ")).   // RAISE 

# if age < 18:
#     raise ValueError("Age must be 18 or above")

# print("You are eligible")

try:
    a = int(input("Enter first: "))
    b = int(input("Enter second: "))

    result = a/b

except ZeroDivisionError:
    print("Cannot divide by zero")

except ValueError:
    print("Invalid input")

else:
    print("Result:", result)

finally:
    print("Execution completed")