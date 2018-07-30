num = [2, 4, 6, 8, 10, 12, 14]
for i in range(len(num) // 2):
    temp = num[i]
    num[i] = num[len(num) - 1 - i]
    num[len(num) - 1 - i] = temp
print(num)
