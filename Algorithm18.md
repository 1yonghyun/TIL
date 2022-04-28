swea 문자열 비교

```
t = int(input())
# 자료에있는거 그대로 쓴다.
for tc in range(1, t + 1):

    p = str(input())
    t = str(input())
    M = len(p)
    N = len(t)

    i = 0
    j = 0


    while j < M and i < N:


        if t[i] != p[j]:
            i = i - j
            j = -1
        i = i + 1
        j = j + 1
    if j == M:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')
```

