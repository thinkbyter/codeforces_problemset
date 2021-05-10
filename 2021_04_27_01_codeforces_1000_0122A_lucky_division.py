# https://codeforces.com/problemset/problem/122/A
# Difficulty: 1000
# Attempts: 1
# Date: 2021-04-27
# Time: 00:38:05

import math
import itertools

n = int(input())

to = int(math.sqrt(n))

o = 'NO'
ndigits = 1
greater = False 
while o == 'NO' and not greater:
  for digits in itertools.product([4, 7], repeat=ndigits):
    divisor = 0
    multiplier = 1
    for i in range(ndigits):
      divisor += multiplier * digits[i]
      multiplier *= 10
    
    if divisor <= n:
      if n % divisor == 0:
        o = 'YES'
        break
    else:
      greater = True
      
  ndigits += 1

print(o)