# 암기왕
# 속도: 리스트 <<< 집합
import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    one = set(map(int, sys.stdin.readline().split()))
    m = int(sys.stdin.readline())
    two = list(map(int, sys.stdin.readline().split()))
    for o in two:
        if o in one:
            print(1)
        else:
            print(0)
