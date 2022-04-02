```
swea 0214연습문제1

t = int(input())
for case in range(t):
    n = int(input())
    lst = [list(map(int,input().split())) for _ in range(n)]
    ans = 0
    # 델타탐색
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(5):
        for j in range(5):
            for d in range(4):
                x = i + dx[d]
                y = j + dy[d]
                if 0 <= x < n and 0 <= y < n:
                    ans += abs(lst[x][y] - lst[i][j])
    print(f'#{case + 1} {ans}')

```