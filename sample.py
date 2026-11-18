# # first = "Hello" #strconcat
# # second = "World"

# # first+=" "+"python"
# # print(first)

# # test="Hello World"   #strrepeat
# # test=test*3
# # print(test)

# # #str compare (==, !=, <, >, <=, >=) with lexicographic order
# # print("Hello" == "Hello")  # True
# # print("Hello" != "World")  # True
# # print("Hello" < "World")   # True
# # print("Hello" > "World")   # False
# # print("Hello" <= "World")  # True
# # print("Hello" >= "World")  # False
# # print("apple" >= "apply")  

# # price = 100.56567
# # print("Price: {:.2f}".format(price))  # Output: Price: 100.57

# # number = 42
# # print("Number: {:d}".format(number))  # Output: Number: 42

# # percentage = 10.123456789
# # print("Percentage: {:.0%}".format(percentage))  # Output: Percentage: 12.3400000%

# # num=10
# # print(bin(num))  # Output: 0b1010
# # print("Number: {:b}".format(num))  # Output: Number: 1010
# # print("Number: {:o}".format(num))  # Output: Number: 12
# # print("Number: {:x}".format(num))  # Output: Number: a
# # print("Number: {:05d}".format(num))  # Output: Number: 0000000000010
# # print("Number: {:5d}".format(num))  # Output: Number: 0000000000010
# # print("Number: {:>15d}".format(num))  # Output: Number:              10
# # print("Number: {:<15d}".format(num))  # Output: Number:              10
# # print("Number: {:^15d}".format(num))  # Output: Number:              10

# # #Escape sequences
# # print("Hello\nWorld")  # Output: Hello (new line) World
# # print("Hello\tWorld")  # Output: Hello (tab) World
# # print("Hello\\World")  # Output: Hello\World
# # print(r"Hello\nWorld")  # Output: Hello\nWorld
# # print("Hello\"World\"")  # Output: Hello"World"
# # print("Hello\'World\'")  # Output: Hello'World'
# # print("Hello\bWorld")  # Output: HelloWorld (backspace removes the character before it)
# # print("vipinkumar\rsharma")  # Output: kumarr sharma (carriage return moves the cursor to the beginning of the line)
# # str = "A"
# # str1 = 'a'
# # str2 = "😃"

# # print(ord(str))  # Output: 65 (ASCII value of 'A')
# # print(ord(str1))  # Output: 97 (ASCII value of 'a')
# # print(ord(str2))  # Output: 128515 (Unicode value of '😃')
# # print("\u0041")     # A
# # print("\u0061")     # a
# # print("\u0905")     # अ
# # print("\u20B9")     # ₹
# # print("\U0001F600") # 😀
# # mixed = [10, "Hello", 3.14, True]
# # print(mixed)
# # for i in mixed:
# #     print(i)

# # list1 = [1, 2, 3, 4, 5]
# # list2=list1
# # print(list1)
# # # list1.append(6)  # This will raise an AttributeError since tuples are immutable
# # list1.append(6)  # This will raise an AttributeError since tuples are immutable
# # print(list1)  # Output: [1, 2, 3, 4, 5, 6]
# # print(list1 is list2)
# arr = [10, 20,20,20, 30]  # Create a list with initial elements

# arr.append(40)          # [10, 20, 30, 40] 
# arr.extend([50, 60])    # [10, 20, 30, 40, 50, 60]
# arr.insert(1, 15)       # [10, 15, 20, 30, 40, 50, 60]

# # arr.remove(20)          # Removes 20
# arr.pop()               # Removes and returns 60
# arr.pop(2)              # Removes and returns the element at index 2
# print(arr)                # [10, 15, 20, 40, 50]
# print(arr.index(20))    # 2
# print(arr.count(10))    # 1

# # arr.sort()              # Ascending order
# arr.reverse()           # Reverse order

# new_arr = arr.copy()    # Shallow copy
# arr.clear()             # []
# print(len(arr))         # 0
# print(len(new_arr))     # 7
# print(max(new_arr))     # 50
# print(min(new_arr))     # 10
# print(sum(new_arr))     # 175
# new_list = sorted(new_arr)    # [10, 15, 30, 40, 50]
# print(new_list)             # [10, 15, 30, 40, 50]
# print(any(new_arr))         # True if any element is True important
# print(all(new_arr))         # True if all elements are True important
# print(new_arr)   
# new_arr.sort()      # Descending order
            
# print(new_arr)                  # [50, 40, 30, 20, 15, 10]


