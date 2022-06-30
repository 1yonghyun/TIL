SWEA 달팽이 숫자

```
T = int(input())

# row, collumn 으로 구분, 우, 하, 좌, 상 방향으로 이동시킨다
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

for tc in range(1, T + 1):
    N = int(input())
    snail = [[0] * N for _ in range(N)]
    # 초기 위치(row, collumn)
    r, c = 0, 0
    # 방향 우, 하, 좌, 상 순으로 바뀐다
    dir = 0

    for n in range(1, N * N + 1):
        snail[r][c] = n
        r += dr[dir]
        c += dc[dir]

        # 방향을 바꾸는 상황을 설정한다. 방향을 바꾸기 전에 기존 인덱스를 빼고 다시 더한다
        if r < 0 or c < 0 or r >= N or snail[r][c] != 0:
            # 기존 값 원위치
            r -= dr[dir]
            c -= dc[dir]
            # 방향 바꾸기, 인덱스의 범위는 0에서 3까지만 설정
            dir = (dir + 1) % 4
            # 바꾼 방향을 적용시킨다.
            r += dr[dir]
            c += dc[dir]

    print(f'#{tc}')
    for row in snail:
        print(*row)
```



