# 1. Creating Sets

s = {10, 20, 30, 40, 20, 10}

print("Original Set:", s)
print("Type:", type(s))

# Empty Set
empty = set()
print("Empty Set:", empty)

# Set with different data types
s1 = {10, "Prince", 20.5, True}
print("Mixed Set:", s1)

# 2. Adding Elements

# add() - Adds one element
s.add(50)
print("After add:", s)

# update() - Adds multiple elements
s.update([60, 70, 80])
print("After update:", s)

# 3. Removing Elements

# remove() - Removes element, error if not found
s.remove(20)
print("After remove:", s)

# discard() - Removes element, no error if not found
s.discard(100)
print("After discard:", s)

# pop() - Removes and returns an arbitrary element
removed = s.pop()
print("Popped Element:", removed)
print("After pop:", s)

# 4. Clearing Set

temp = {1, 2, 3}
temp.clear()
print("After clear:", temp)

# 5. Built-in Functions

numbers = {10, 20, 30, 40, 50}

print("Length:", len(numbers))
print("Maximum:", max(numbers))
print("Minimum:", min(numbers))
print("Sum:", sum(numbers))
print("Sorted:", sorted(numbers))

# 6. Membership Operators

print("20 in set:", 20 in numbers)
print("100 not in set:", 100 not in numbers)

# 7. Set Operations

A = {10, 20, 30, 40}
B = {30, 40, 50, 60}

# Union - Combines both sets
print("Union:", A.union(B))
print("Union using |:", A | B)

# Intersection - Common elements
print("Intersection:", A.intersection(B))
print("Intersection using &:", A & B)

# Difference - Elements in A but not in B
print("Difference:", A.difference(B))
print("Difference using -:", A - B)

# Symmetric Difference - Elements not common
print("Symmetric Difference:", A.symmetric_difference(B))
print("Symmetric Difference using ^:", A ^ B)

# 8. Updating Set Operations

C = {10, 20, 30}
D = {20, 30, 40}

C.update(D)
print("After union update:", C)

C = {10, 20, 30}
C.intersection_update(D)
print("After intersection update:", C)

C = {10, 20, 30}
C.difference_update(D)
print("After difference update:", C)

C = {10, 20, 30}
C.symmetric_difference_update(D)
print("After symmetric difference update:", C)

# 9. Set Comparison Methods

X = {10, 20}
Y = {10, 20, 30, 40}
Z = {50, 60}

print("Is subset:", X.issubset(Y))
print("Is superset:", Y.issuperset(X))
print("Is disjoint:", X.isdisjoint(Z))

# 10. Copy Method

original = {1, 2, 3}
copied = original.copy()

print("Original:", original)
print("Copied:", copied)

