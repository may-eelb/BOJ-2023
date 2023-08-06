from sys import stdin
input = stdin.readline
import math

n , m = map(int ,input().split())
gcd = math.gcd(n, m)
print(m - gcd)