'''
sample_list = [1,1,2,2,3,3]


sample_set = set(sample_list)

print(sample_set)

myset = set([])
myset.add(5)
myset.add(6)
myset.add(4)
myset.add(2)
myset.add(1)

print(myset)

myset.remove(2)

myset.discard(5)


a = {1,2,3,4,5}
b = {4,5,6,7,8}

# Union of Ssts
print(a | b)

# Intersection of Sets
print(a & b)

# Difference of Sets
print(a - b)

# Symmetric Difference of Sets
print(a ^ b)
'''




x = {50, 51, 52, 53, 54, 55}
Y = {55, 56, 57 ,58, 59}

# Union of Ssts
print(x | Y)

# Intersection of Sets
print(x & Y)

# Difference of Sets
print(x - Y)

# Symmetric Difference of Sets
print(x ^ Y)