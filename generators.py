import numpy as np

'''
First, we're going to create a list containing the units of Z_n
'''

n = int(input("Enter desired n: "))
zn = []

for i in range(n + 1):
  if np.gcd(i, n) == 1: # check if i is coprime to n
    zn.append(i)

print(f"(Z_{n})*: {zn}")

'''
Now we want to see if k in zn to the power of j in [1, n] produces the same list as zn
'''

generators = []

for k in zn:
  temp = set({})

  for j in range(n + 1):
    temp.add((k**j) % n)

  if sorted(list(temp)) == zn:
    generators.append(k)

if generators == []:
    print(f"(Z_{n})* has no generators")
else:
    print(f"Generators of (Z_{n})*: {generators}")