swea 민석이의 과제 체크

```
T = int(input())

for tc in range(1, T + 1):
    # 학생수, 제출한 사람 수
    num, submit = map(int, input().split())
    # 제출한 사람
    lst1 = list(map(int, input().split()))
    # 제출 안한 사람
    lst2 = []
    # 제출한 사람에 해당하지 않는다면 lst2에 추가
    for i in range(1, num + 1):
        if i not in lst1:
            lst2.append(i)

    print(f'#{tc}', end=' ')
    print(*lst2)

```

