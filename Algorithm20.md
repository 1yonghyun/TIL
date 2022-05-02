swea 부분집합의 합

```
T = int(input())
for tc in range(1, 1 + T):
    n, k = map(int, input().split())
    lst = list(range(1, 13))
    cnt = 0
    for i in range(1<<n):
        tmp_lst = []
        tmp = 0
        for j in range(n):
            if i and (1<<j):
                tmp_lst.append(lst[j])
                tmp += lst[j]
        if tmp == k and len(tmp_lst) == n:
            cnt += 1
    print(f'#{tc} {cnt}')
```

