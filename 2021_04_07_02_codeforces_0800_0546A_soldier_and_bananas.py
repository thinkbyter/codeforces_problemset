# https://codeforces.com/problemset/problem/546/A
# Difficulty: 800
# Attempts: 1
# Date: 2021-04-07
# Time: 00:05:36

k, n, w = map(int, input().split())

cost = 0
for i in range(1, w + 1):
  cost += i * k
  
print(max(0, cost - n))