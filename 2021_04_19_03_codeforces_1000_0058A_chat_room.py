# https://codeforces.com/problemset/problem/58/A
# Difficulty: 1000
# Attempts: 1
# Date: 2021-04-19
# Time: 00:05:38

import re

s = input()

o = 'NO'
p = re.compile('.*h.*e.*l.*l.*o.*')
if p.match(s):
  o = 'YES'
  
print(o)