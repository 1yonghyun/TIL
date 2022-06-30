```
t = int(input())
for case in range(t):
    n = int(input())
    lst = [list(map(int,input().split())) for _ in range(n)]
# print(lst)
# 벽에 있는 요소는 어떻게 쓸것인가?
    ans = 0
    # 우선 벽에 없는 요소부터 쓴다
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(5):
        for j in range(5):
            for d in range(4):
                x = i + dx[d]
                y = j + dy[d]
                if 0 <= x < n and 0 <= y < n :
                    ans += abs(lst[x][y] - lst[i][j])
            #ans += abs(lst[i][j - 1] - lst[i][j]) + abs(lst[i - 1][j] - lst[i][j]) + abs(lst[i][j + 1] - lst[i][j]) + abs(lst[i + 1][j] - lst[i][j])

    # lst[0][0], lst[0][4], lst[4][0], lst[4][4] 일때
    ans += abs(lst[0][0] - lst[0][1]) + abs(lst[0][0] - lst[1][0])

    ans += abs(lst[0][4] - lst[0][3]) + abs(lst[0][4] - lst[1][4])

    ans += abs(lst[4][0] - lst[4][1]) + abs(lst[4][0] - lst[3][0])

    ans += abs(lst[4][4] - lst[4][3]) + abs(lst[4][4] - lst[3][4])

    # 위쪽 벽에 있는 요소
    for j in range(1, 4):
        ans += abs(lst[0][j + 1] - lst[0][j]) + abs(lst[1][j] - lst[0][j]) + abs(lst[0][j - 1] - lst[0][j])
    # 아래쪽 벽에 있는 요소
    for j in range(1, 4):
        ans += abs(lst[4][j + 1] - lst[4][j]) + abs(lst[4][j - 1] - lst[4][j]) + abs(lst[3][j] - lst[4][j])
    # 왼쪽 벽에 있는 요소
    for i in range(1, 4):
        ans += abs(lst[i - 1][0] - lst[i][0]) + abs(lst[i + 1][0] - lst[i][0]) + abs(lst[i][1] - lst[i][0])
    # 오른쪽 벽에 있는 요소
    for i in range(1, 4):
        ans += abs(lst[i - 1][4] - lst[i][4]) + abs(lst[i + 1][4] - lst[i][4]) + abs(lst[i][3] - lst[i][4])

    print(ans)
```

