swea 이진탐색

```
def binarysearch(N, key):
    start = 1
    end = N
    cnt = 0
    while start <= end:
        middle = (start + end)//2
        if middle == key:
            cnt += 1
            return cnt
        elif middle > key:
            cnt += 1
            end = middle
        else:
            cnt += 1
            start = middle
    return 0


T = int(input())

for tc in range(1, 1 + T):
    p, pa, pb = map(int, input().split())
    a = binarysearch(p, pa)
    b = binarysearch(p, pb)
    if a > b:
        ans = 'B'
    elif a < b:
        ans = 'A'
    else:
        ans = 0
    print(f'#{tc} {ans}')
```

