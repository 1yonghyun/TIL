swea 삼성시의 버스노선

```
T = int(input())
for tc in range(1, 1 + T):
    N = int(input())
    # cnt 세는 리스트 만들기
    lst = [0] * 5001
    for i in range(1, 1 + N):
        A, B = map(int, input().split())
        for j in range(A, B + 1):
            lst[j] += 1
    P = int(input())
    ans = []
    for i in range(P):
        ans.append(lst[int(input())])
    print(f'#{tc}', *ans)
```

