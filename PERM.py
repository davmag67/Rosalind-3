from itertools import permutations
n=3
if n>7:
    raise Exception('The number cannot be higher than 7')
# Create a list with first n numbers
num_list=list(range(1,n+1))
#print(num_list)
# The total number of permutations is equal to the factorial of n
# Definition of a function that calculates the factorial of a number n
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
#################################################################
n_perm=factorial(n)
perm=permutations(num_list)
print(n_perm)
for i in list(perm):
    print(i)