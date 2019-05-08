import math

result = 0
x = int(input())
for i in range(1,x,1):
    if (i%5 == 0) or (i%3==0):
        result = result + i
        
print(result)
