swea 가장빠른문자열타이핑

```
a = int(input())

for tc in range(1, a + 1):

    p, t = map(str, input().split())

    M = len(p)
    N = len(t)

    i = 0
    j = 0

    cnt = 0
    while j < M and i < N:


        if t[i] != p[j]:
            i = i - j
            j = -1
        i = i + 1
        j = j + 1
        if j == M:
            cnt += 1
            print(cnt)
            j = 0



    print(f'#{tc} {M - (N - 1) * cnt}')
```

