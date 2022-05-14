swea 의석이의 세로로 말해요

```
T = int(input())
for tc in range(1, 1 + T):
    arr = [list(input()) for _ in range(5)]
    lst = []
    # print(f'#{tc}', end=' ') 이방식은 안된다
    # 문자열 최대 길이인 15만큼 순회한다
    for j in range(15):
        # 문자열 개수 5개만큼 순회
        for i in range(5):
            # 문자열의 인덱스가 문자열의 길이보다 작을때만 리스트에 추가한다
            if j < len(arr[i]):
                # print(arr[i][j], end='')
                lst.append(arr[i][j])
    print(f'#{tc} {"".join(lst)}')
```

