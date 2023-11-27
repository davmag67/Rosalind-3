'''
A set with n elements can be grouped in subsets applying a mask of a binary code 0 and 1
The mask will have the same lenght of n and will be a sequence of 0 and 1
the position corresponding to 1 will indicate the presence in the subset of that specific element
for example a subset of 2 elements (a,b) can be mapped to the sequence XY where X and Y can be either 0 or 1.
Therefore: 
    - 11 will indicate the subset including both a and b
    - 10 will indicate the presence of only a
    - 01 will indicate the presence of only b
    - 00 will indicate the empty subset
In a similar way we can map a 3 elements set (a,b,c) with 111, 110, 101, etc.
All possible subsets will be 2 to the power of n.
'''
n=3
if n>1000:
    raise Exception('n cannot be higher than 1000')
result=(2**n)%1000000
print(result)
