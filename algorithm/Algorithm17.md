swea 문자열 비교

```
T = int(input())

for tc in range(1, 1 + T):
    str1 = list(input())
    str2 = list(input())
    word_length = len(str1)
    sentence_length = len(str2)
    # 문장 인덱스
    i = 0
    # 단어 인덱스
    j = 0
    ans = 0
    while i < sentence_length and j < word_length:
        if str2[i] != str1[j]:
            i -= j
            j = -1
        i += 1
        j += 1
        if j == word_length:
            ans = 1
    print(f'#{tc} {ans}')
```

