# https://codeforces.com/problemset/problem/977/A
# Difficulty: 800
# Attempts: 2
# Date: 2021-04-07
# Time: 00:16:40

n, k = map(int, input().split())

while k > 0:
  r = n % 10
  if r == 0:
    n //= 10
    k -= 1
  else:
    s = min(k, r)
    n -= s
    k -= s
    
print(n)