# https://codeforces.com/problemset/problem/158/A
# Difficulty: 800
# Attempts: 2 
# Date: 2021-04-04
# Time: 00:24:40

m, n = map(int, input().split())

res = (m // 2) * (n // 2) * 2

if m % 2 == 1:
  res += n // 2
if n % 2 == 1:  
  res += m // 2
  
print(res)