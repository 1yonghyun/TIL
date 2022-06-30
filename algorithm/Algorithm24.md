swea 숫자카드

```
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    lst1 = list(map(int, input()))
    lst2 = [0] * 10
    # lst1안의 숫자 확인하고 개수 세기
    for i in lst1:
        lst2[i] += 1
    # 가장 높은 수
    cardmax = 0
    # 가장 높은 수의 개수
    cardmax_num = 0
    for i in range(10):
        if lst2[i] >= cardmax_num:
            cardmax_num = lst2[i]
            cardmax = i
    print(f'#{tc} {cardmax} {cardmax_num}')
```

