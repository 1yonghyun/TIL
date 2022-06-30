swea flatten

```
import sys
sys.stdin = open('input.txt')
# 이전 풀이가 왜 안됐는지는 잘 모르겠다.
# index함수를 활용한 풀이다.
for tc in range(1, 11):
    # input
    dump = int(input())
    lst = list(map(int, input().split()))
    # 최대값, 최소값 설정
    minv = maxv = lst[0]
    for i in range(dump):
        # for j in range(100):
        #     if lst[j] > maxv:
        #         maxv = lst[j]
        #     if lst[j] < minv:
        #         minv = lst[j]
        maxv = max(lst)
        minv = min(lst)
        # 이렇게 해야 리스트안의 값이 바뀐다
        lst[lst.index(maxv)] -= 1
        lst[lst.index(minv)] += 1
    # 최대값, 최소값 차이의 값이 정답이다
    maxv = max(lst)
    minv = min(lst)
    ans = maxv - minv
    print(f'#{tc} {ans}')
```

