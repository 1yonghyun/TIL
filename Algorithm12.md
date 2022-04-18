swea 구간합

```
T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))
    maxv = 0
    minv = 999999
    for i in range(N - M + 1):

        tmp = 0
        for j in range(M):
            tmp += lst[i + j]
        if tmp > maxv:
            maxv = tmp
        if tmp < minv:
            minv = tmp
    ans = maxv - minv
    print(f'#{tc} {ans}')

```

