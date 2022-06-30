swea 특별한 정렬

```
T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    num = list(map(int, input().split()))
    lst = []
#    print(min(num), max(num))
    for i in range(10):
        if i % 2:
            lst.append(min(num))
            num.remove(min(num))
        else:
            lst.append(max(num))
            num.remove(max(num))
    # print(f'#{tc}', end=' ')
    # print(*lst)
    print(f'#{tc}', *lst[:10])

```

