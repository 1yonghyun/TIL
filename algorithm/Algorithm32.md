swea 현주의 상자바꾸기

```
T = int(input())

for tc in range(1, 1 + T):
    # N은 상자 개수, Q는 작업 횟수
    N, Q = map(int, input().split())
    # 정답이 될 lst만들기
    lst = [0] * N
    for i in range(Q):
        L, R = map(int, input().split())
        #인덱스 맞추려면 1을 뺴줘야한다.
        for j in range(L - 1, R):
            # i도 0부터 시작하기 때문에 1을 더해줘야한다
            lst[j] = i + 1
    print(f'#{tc}', *lst)
```

