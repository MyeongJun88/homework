numbers=[]
i=1
while i<=10:
    numbers.append(i)
    i+=1
print(numbers)

i=0
while i < len(numbers):
    if numbers[i] % 2 == 1:
        del numbers[i]
    else:
        i += 1
print(numbers)

numbers.insert(0, 20)
print(numbers)

print(sorted(numbers))