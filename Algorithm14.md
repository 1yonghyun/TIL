swea 글자수

```
T = int(input())
for tc in range(1, T + 1):
    str1 = set(str(input()))
    str2 = str(input())

    cnt = 0
    for i in str1:
        tmp = 0
        for j in str2:
            if i == j:
                tmp += 1
                if tmp > cnt:
                    cnt = tmp
    print(f'#{tc} {cnt}')
```

