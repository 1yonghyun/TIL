1. abs(), aiter(), all(), any(), anext()



2. s = 'ssafy'

   def solution(s):

   ​		return s[(len(s)-1)//2:len(s)//2 + 1]

   print(solution(s))

   print(solution('coding'))



3.  (4)



4. 10



5. def my_avg(*ints):

   ​		sum = 0

   ​		for num in ints:

   ​				sum += num

   ​		return sum

   print(my_avg(77, 83, 95, 80, 70))