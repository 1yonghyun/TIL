swea 민석이의 과제 제출

```
# testcase 숫자
T = int(input())
for tc in range(1, T + 1):
    # 수강생의 수, 과제 제출한 사람의 수
    N, K = map(int, input().split())
    # 과제 제출한 사람의 번호
    lst = list(map(int, input().split()))
    # 제출 안한 사람 리스트
    ans = []
    # 1 부터 N까지의 숫자 중에 없는 숫자가 정답이다
    for i in range(1, 1 + N):
        # 없는 숫자는 정답에 포함시킨다
        if i not in lst:
            ans.append(i)
    # 한칸 띄어서 출력
    print(f'#{tc}', *ans)
```

