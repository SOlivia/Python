import math

total = 0
count = 0
result = 0
i = 0
while i != -1:
    i = float(input())
    if i != -1:
        total = total + i
        count = count + 1
        result = total / count

print(result)
