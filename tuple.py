# 1. Creating Tuples
t = (10, 20, 30, 20, 40, 50)

print("Original Tuple:", t)
print("Type:", type(t))

# 2. Tuple Methods

# count() - Counts occurrences
print("Count of 20:", t.count(20))

# index() - Finds first occurrence
print("Index of 30:", t.index(30))

# 3. Built-in Functions

print("Length:", len(t))
print("Maximum:", max(t))
print("Minimum:", min(t))
print("Sum:", sum(t))
print("Sorted:", sorted(t))
print("Reversed:", tuple(reversed(t)))

# 4. Indexing

print("First Element:", t[0])
print("Last Element:", t[-1])

# 5. Slicing

print("Elements 1 to 3:", t[1:4])
print("First Three:", t[:3])
print("Reverse Tuple:", t[::-1])

# 6. Tuple Operations

t1 = (10, 20, 30)
t2 = (40, 50, 60)

# Concatenation
print("Concatenation:", t1 + t2)

# Repetition
print("Repetition:", t1 * 2)

# Membership
print("20 in tuple:", 20 in t1)
print("100 not in tuple:", 100 not in t1)

# 7. Tuple Unpacking

a, b, c = t1

print("Unpacking:")
print(a)
print(b)
print(c)

# 8. Conversion

# List to Tuple
my_list = [1, 2, 3, 4]
new_tuple = tuple(my_list)

print("List to Tuple:", new_tuple)

# Tuple to List
new_list = list(t1)
new_list.append(40)

print("Tuple to List:", new_list)

# 9. any() and all()

t3 = (0, 0, 10, 0)
t4 = (10, 20, 30, 40)

print("Any:", any(t3))
print("All:", all(t4))

# 10. Single Element Tuple

single = (10,)
print("Single Element:", single)
print("Type:", type(single))

# 11. Immutable Property

# Tuples cannot be modified directly.
# t1[0] = 100  # TypeError

print("Tuple is Immutable")
