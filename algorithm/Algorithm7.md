```
for tc in range(10):
    n = int(input())
    # str으로 input 받기
    word = str(input())
    sentence = str(input())
    word_length = len(word)
    sentence_length = len(sentence)
    cnt = 0
    # sentence의 인덱스
    i = 0
    # word의 인덱스
    j = 0
    while j < word_length and i < sentence_length:
        if sentence[i] != word[j]:
            i = i - j
            j = -1
        i += 1
        j += 1
        if j == word_length:
            cnt += 1
            j = 0
    print(f'#{n} {cnt}')
```

swea string