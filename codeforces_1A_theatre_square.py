# https://codeforces.com/problemset/problem/1/A
# Difficulty: 1000
# Trials: 1
# Time: 00:03:33

n, m, a = map(int, input().split())

print((n // a + (0 if n % a == 0 else 1)) * (m // a + (0 if m % a == 0 else 1)))