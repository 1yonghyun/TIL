1. ```python
   k = int(input())
   for i in range(1, k+1):
       if k % i == 0:
           print(i, end=' ')
   ```





2. ```python
   import statistics
   
   print(statistics.median(numbers))
   ```



3. ```python
   a = int(input())
   
   for i in range(1, a+1):
       for k in range(1, i+1):
           print(k, end=' ')
       print()
   ```