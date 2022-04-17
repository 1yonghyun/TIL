swea 고대유적

```
T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    # 가로, 어차피 최소 2칸이기 때문에 이전칸에 1이었고 현재칸에 1이라면 2칸이라는 답이 나오도록 설정
    for i in range(N):
        tmp = 1
        for j in range(1, M):
            if arr[i][j - 1] == 1 and arr[i][j] == 1:
                tmp += 1
                if tmp > ans:
                    ans = tmp
            else:
                tmp = 1

    # 세로
    for i in range(M):
        tmp = 1
        for j in range(1, N):
            if arr[j - 1][i] == 1 and arr[j][i] == 1:
                tmp += 1
                if tmp > ans:
                    ans = tmp
            else:
                tmp = 1
    print(f'#{tc} {ans}')
```

