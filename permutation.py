#generator
from itertools import permutations
def double_it (val):
    print('double it')
    return val*2

nums=range(10)
comp=(double_it(x) for x in nums)
#print(comp)

# for i in comp:
#     print(i)

perm=permutations(range(10),4)
for i in perm:
    print(i)

print(len(list(perm)))