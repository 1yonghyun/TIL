swea 회문문제

```
t = int(input())

for tc in range(1, t + 1):
    # input
    N, M = map(int, input().split())
    lst = [list(input()) for _ in range(N)]

    # # 가로 검색
    # for i in range(n):
    #     for j in range(m):
    #         if n[::-1][i] == n[i]:

# 회문은 좌우대칭
# 전체를 P라 할때 for i in range(P//2)
# if P[i] !=

# for M in range(100, 1, -1):
    # 가로
    print(f'#{tc}', end=' ')
    for i in range(N):
        for j in range(N - M + 1):
            tmp = 0
            for k in range(M // 2):

               # lst[i][j] ~ lst[i][j + M]

            # 확인하는 방법은 lst[i][j:j+M] == lst[i][j:j+M][::-1]

                if lst[i][j + k] != lst[i][j + M - 1 - k]:
                   break
                else:
                    tmp += 1
            if tmp == M // 2:
                for l in range(j, j + M):
                    print(lst[i][l], end='')

    # 세로
    for i in range(N):
        for j in range(N - M + 1):
            tmp = 0
            for k in range(M//2):
                if lst[j + k][i] != lst[j + M - 1 - k][i]:
                    break
                else:
                    tmp += 1
            if tmp == M // 2:
                for l in range(j, j + M):
                    print(lst[l][i], end='')
    print()
```

