#Use the itertools module and product function to find the Cartesian product of the input variables A and B. If only A is provided, then we need to provide an argument repeat=X, where X = the number of coordinates in the tuple.
# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product
A = raw_input().split()
B = raw_input().split()
arr = []
product = list(product(A, B))
for tpl in product:
    print (int(tpl[0]), int(tpl[1])),
