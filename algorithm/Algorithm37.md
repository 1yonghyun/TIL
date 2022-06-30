swea flatten

```
for tc in range(1, 11):
    dump = int(input())
    lst = list(map(int, input().split()))

    min_v = max_v = lst[0]
    # lst에서 최대 최소값 구하기(min, max함수 써도 상관없다)
    for k in range(dump):
        for j in range(len(lst)):
            if lst[j] > max_v:
                max_v = lst[j]
            if lst[j] < min_v:
                min_v = lst[j]

        # dump하면 최대값에서 1빼고 최소값에 1더한다
        max_v -= 1
        min_v += 1
    print(f'#{tc} {max_v - min_v}')
```

