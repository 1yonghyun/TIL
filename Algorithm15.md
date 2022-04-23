```
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [[0]*N for _ in range(N)]

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    cnt = 1
    i = 0
    j = 0
    x = 0
    y = 0
    arr[y][x] = cnt
    while cnt < N * N:

        # cnt += 1
        x = x + dx[i]
        y = y + dy[j]
        if 0 <= x < N and 0 <= y < N and arr[y][x] == 0:
            cnt += 1
            arr[y][x] = cnt
        else:

            x -= dx[i]
            y -= dy[j]
            i = (1 + i)%4
            j = (1 + j)%4

    print(f'#{tc}')
    for lst in arr:
        print(*lst)
```

