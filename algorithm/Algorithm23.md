swea 쇠막대기 자르기

```
T = int(input())

for tc in range(1, 1 + T):
    lst = list(input())
    cnt = ans = 0
    for i in range(len(lst)):
        # ( 일때 cnt 증가, 이후에 쇠막대기인 경우와 레이져인 경우로 나눈다
        if lst[i] == '(':
            cnt += 1
        else: # )인 경우
            if lst[i - 1] == '(': # 바로 앞에 괄호라면 레이져이다, 레이져 한번당 쇠막대기 개수만큼 답이 증가한다
                cnt -= 1
                ans += cnt
            else: # 쇠막대기인 경우다, 쇠막대기당 ans가 1씩 증가한다, (일때마다 ans += 1해도 되지만 그러면 레이져일때 ans -= 1해줘야 할거다
                cnt -= 1
                ans += 1
    print(f'#{tc} {ans}')
```

