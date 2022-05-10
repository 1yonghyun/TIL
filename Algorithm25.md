swea 연속한 1의 개수

```
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input()))
    ans = 0
    tmp = 0
    # 리스트 순회
    for i in range(N):
        # 1이라면 tmp증가
        if lst[i] == 1:
            tmp += 1
            # ans에 최대값 부여
            if tmp > ans:
                ans = tmp
        # tmp 초기화
        else:
            tmp = 0
    print(f'#{tc} {ans}')
```

