```
for tc in range(1, 11):
    a = int(input())
    p = str(input())
    t = str(input())
    M = len(p)
    N = len(t)

    i = 0
    j = 0

    cnt = 0
    while j < M and i < N:

# 만약 일치하지 않다면 인덱스를 되돌림
        if t[i] != p[j]:
            i = i - j
            j = -1
        i = i + 1
        j = j + 1
# 일치하다면 cnt증가
        if j == M:
            cnt += 1
            j = 0



    print(f'#{tc} {cnt}')
```

