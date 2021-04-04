# https://codeforces.com/problemset/problem/71/A
# Difficulty: 800
# Attempts: 1
# Date: 2021-04-04
# Time: 00:04:18

T = int(input())

for _ in range(T):
  w = input()
  if len(w) > 10:
    print(f'{w[0]}{len(w) - 2}{w[-1]}')
  else:
    print(w)