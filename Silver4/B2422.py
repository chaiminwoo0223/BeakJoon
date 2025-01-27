# 한윤정이 이탈리아에 가서 아이스크림을 사먹는데
# 집합과 tuple
import sys

n, m = map(int, sys.stdin.readline().split())
no = set()
count = 0

for _ in range(m):
    no.add(tuple(sorted(map(int, sys.stdin.readline().split()))))

# 완전 탐색
for i in range(1, n-1):
    for j in range(i+1, n):
        for k in range(j+1, n+1):
            if (i, j) not in no and (j, k) not in no and (i, k) not in no:
                count += 1

print(count)
