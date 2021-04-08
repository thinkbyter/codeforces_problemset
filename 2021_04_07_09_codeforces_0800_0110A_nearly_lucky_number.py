# https://codeforces.com/problemset/problem/110/A
# Difficulty: 800
# Attempts: 1
# Date: 2021-04-07
# Time: 00:03:36

n = input() 
l = n.count('4') + n.count('7') 

if l == 4 or l == 7:
  print('YES')
else:
  print('NO')