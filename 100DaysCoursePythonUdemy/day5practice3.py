total = 0
for numb in range (2, 101, 2):
    total += numb
print(total)

total2 = 0
for numb2 in range(1, 101):
    if numb2 % 2 == 0:
        total2 += numb2
print(total2) 
