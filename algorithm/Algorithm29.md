swea 점점 커지는 당근의 개수

```
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input().split()))
    ans = 1
    tmp = 1
    # 이전 당근보다 연속으로 크다면 당근 개수 추가
    for i in range(1, N):
        if lst[i] > lst[i - 1]:
            tmp += 1
            if tmp > ans:
                ans = tmp
        else:
            tmp = 1
    print(f'#{tc} {ans}')
```

