swea 글자수

```
T = int(input())

for tc in range(1, T + 1):
    #input 받기
    a = str(input())
    b = str(input())
    #리스트 만들어서 개수 구하기
    lst = [0]*len(a)
    # 밖에 없으면 초기화가 계속된다
    max = 0
    for i in range(len(a)):
        # 가장 큰 값 설정


#       a에 있는 문자와 b에 있는 문자가 동일하면 lst 숫자 증가
        for j in range(len(b)):
            if a[i] == b[j]:
                lst[i] += 1

        # 리스트에서 가장 큰 값 구하기
        if max < lst[i]:
            max = lst[i]

    print(f'#{tc} {max}')
```

