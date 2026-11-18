text = "meet"
print(text.upper())
print(text.lower())
print(text.capitalize())
print(text.title())
print(text.strip())
print(text.replace("e", "a"))
print(text.split("e"))
print(text.join(["m", "e", "e", "t"]))
print(text.find("e")) #it return -1 if value not present
print(text[-1]) #it return last character
print(text.count("e"))
for i in range(len(text)):
    print(text[i])

print("startwith('m'):", text.startswith('m'))
print("endswith('t'):", text.endswith('t'))  
print("/".join(text)) #it will join the string with - between each character
list1 = ["hello", "world", "python"]
print(" ".join(list1)) #it will join the list with space between each element
string1 = "helloworld"
print(string1.split(" ")) #it will split the string with space between each character

print("\u0041")
print("\u0042")
print("\u20B9")
print("\U0001F600")
