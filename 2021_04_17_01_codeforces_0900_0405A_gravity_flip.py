# https://codeforces.com/problemset/problem/405/A
# Difficulty: 900
# Attempts: 1
# Date: 2021-04-17
# Time: 00:19:10

n = int(input())
ax = list(map(int, input().split()))
ax.sort()
print(' '.join(map(str, ax)))