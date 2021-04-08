# https://codeforces.com/problemset/problem/339/A
# Difficulty: 800
# Attempts: 1
# Date: 2021-04-05
# Time: 00:03:33

xs = list(map(int, input().split('+')))
xs.sort()
print('+'.join(map(str, xs)))