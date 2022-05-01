```
import sys
sys.stdin = open("sample_input(1).txt")
#테스트 케이스 개수
T = int(input())
for tc in range(1, T+1):
    #N과 K 받기
    N, K = map(int, input().split())
# A는 1부터 12까지의 숫자
    # arr = list(range(1, 13))
    A = [ i for i in range(1, 13)]
    result = 0


    for i in range(1<<12):
        # 부분집합의 합 설정
        tmp_cnt = 0
        tmp_sum = 0


        for j in range(12):

            if i & (1<<j):
                #부분집합의 합을 변환했을 때 개수를 세기
                #부분집합의 합
                tmp_sum += A[j]
                tmp_cnt += 1
                #부분집합의 합이 K일떄 출력
        if tmp_sum == K and tmp_cnt == N:
            result += 1
    print(f'#{tc} {result}')

```

