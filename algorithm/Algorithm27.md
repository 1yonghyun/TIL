swea 전기버스

```
T = int(input())
for tc in range(1, T + 1):
    K, N, M = map(int, input().split()) # 이동거리, 종점, 중전기 개수
    charge = list(map(int, input().split())) + [N + K, N + K] # 충전기 위치
    here = 0 # 현재위치
    cnt = 0
    i = 0 # charge의 인덱스
    # 현재위치가 종점보다 작을때만 계속 한다. 현재위치가 종점과 동일할때도 하면 cnt가 또 증가해서 틀리다.
    while here + K < N:
        if here + K >= charge[i + 2]:
            here = charge[i + 2]
            i += 3
            cnt += 1
            continue
        if here + K >= charge[i + 1]:
            here = charge[i + 1]
            i += 2
            cnt += 1
            continue

        elif here + K < charge[i]:
            cnt = 0
            break
        else:
            here = charge[i]
            i += 1
            cnt += 1
    print(f'#{tc} {cnt}')
```

