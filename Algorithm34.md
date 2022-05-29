swea 쉬운 거스름돈

```
for tc in range(int(input())):
    N = int(input())
    # 정답
    ans = []
    # 전부 나누고 몫을 리스트에 추가
    a = N//50000
    ans.append(a)
    N -= a*50000
    b = N//10000
    ans.append(b)
    N -= b*10000
    c = N//5000
    ans.append(c)
    N -= c*5000
    d = N//1000
    ans.append(d)
    N -= d*1000
    e = N//500
    ans.append(e)
    N -= e*500
    f = N//100
    ans.append(f)
    N -= f*100
    g = N//50
    ans.append(g)
    N -= g*50
    h = N//10
    ans.append(h)
    print(f'#{tc + 1}')
    print(*ans)

```

