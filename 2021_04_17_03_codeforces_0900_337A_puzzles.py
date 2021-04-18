# https://codeforces.com/problemset/problem/337/A
# Difficulty: 900
# Attempts: 1
# Date: 2021-04-17
# Time: 00:14:07

n, m = map(int, input().split()) 
fs = list(map(int, input().split()))
fs.sort()

o = min([fs[i + n - 1] - fs[i] for i in range(0, m - n + 1)])
print(o)