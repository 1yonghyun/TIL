swea min max

```
T = int(input())
for tc in range(1,T+1):
    n = int(input()) #자료수
    arr = list(map(int, input().split()))
    #공백기준 잘라낸 문자열의 리스트

    max = 0 #가장 큰 수


    for i in arr:
        #가장 작은 수
        if max < i:
            max = i
        #가장 큰 수
    min = max
    for num in arr:
        if min >= num:
            min = num # min
    # 가장 큰 수와 가장 작은 수의 차이
    ans = max - min

    print(f'#{tc} {ans}')
```

