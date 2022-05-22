swea 전기버스

```
T = int(input())
for tc in range(1, T + 1):
    k, n, m = map(int, input().split())
    data = list(map(int, input().split())) + [n + k, n + k]
    # n 종점 k 이동가능 m 정류장 개수
    here = 0 #내위치
    i = 0 #정류장위치
    cnt = 0#기름 넣을떄 마다 + 1
    while here + k < n:
        if here + k >= data[i+2]:
            here = data[i + 2]
            cnt += 1
            i += 3
            continue
        elif here + k >= data[i + 1]:
            here = data[i + 1]
            cnt += 1
            i += 2
            continue
        elif here + k < data[i]:
            cnt = 0
            break

        else:
            here = data[i]
            cnt += 1
            i += 1
    print(f'#{tc} {cnt}')

```

