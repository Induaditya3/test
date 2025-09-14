from math import comb
level = int(input("input:"))
triangle = lambda n: [comb(n,k) for k in range(n+1)]
print(str(triangle(level)))