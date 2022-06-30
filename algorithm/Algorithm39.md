swea flatten

```
import sys
sys.stdin = open("input.txt")

for tc in range(1, 11):
    dump = int(input())
    lst = list(map(int, input().split()))
    # 인덱스를 구해야 쓸 수 있는 방법이다. 그럼 인덱스를 어떻게 구할 것인가?
    minv = maxv = lst[0]
    for i in range(dump):
    #     max_v = max(lst)
    #     min_v = min(lst)
    #     max_v -= 1
    #     min_v += 1
    #     for j in range(len(lst)):
    #         if lst[j] > maxv:
    #             maxv = lst[j]
    #         if lst[j] < minv:
    #             minv = lst[j]
        # 인덱스 구하는법 찾아 쓰자
        maxv = max(lst)
        minv = min(lst)
        idx_maxv = lst.index(maxv)
        idx_minv = lst.index(minv)
        lst[idx_maxv] -= 1
        lst[idx_minv] += 1
    print(f'#{tc} {max(lst) - min(lst)}')
```

