import itertools
# The collection of symbols will be in a tuple
symbols=('A','C','G','T')
n=2
if len(symbols)>10:
    raise Exception('the max number of symbols must be 10')
if n>10:
    raise Exception('n cannot be higher than 10')
######################################################################
# Use the permutations with repetitions function within itertools
perm = itertools.product(symbols, repeat=n)
# Create a list with strings
list_str=[]
for i in perm:
    s=''
    for j in range(n):
        s=s+i[j]
    list_str.append(s)
# Using the sorted function to print the result
for i in sorted(list_str):
    print(i)
