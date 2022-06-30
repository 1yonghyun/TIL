swea 색칠하기

```
T = int(input())

for tc in range(1, 1 + T):
    n = int(input())
    # 빈칸으로 이차원 배열만들기
    arr = list(['']*10 for _ in range(10))
    # 사각형 수만큼 순회
    for i in range(n):
        x1, y1, x2, y2, c = map(int, input().split())
        # 사각형 범위만큼 R,B 넣기
        for k in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                if c == 1:
                    arr[k][j] += 'R'
                else:
                    arr[k][j] += 'B'
    # R,B 겹치는 범위 개수 세기
    cnt = 0
    for i in range(10):
        for j in range(10):
            if 'R' in arr[i][j] and 'B' in arr[i][j]:
                cnt += 1
    print(f'#{tc} {cnt}')
```

