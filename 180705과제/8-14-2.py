numbers = [2, 4, 6, 8, 10, 12, 14]


for i in range(len(numbers)):
 i=0
 while i < len(numbers)-1 - i:
  temp = numbers[i]
  numbers[i] = numbers[(len(numbers)-1) - i]
  numbers[(len(numbers)-1) - i] = temp
  i+=1

print("뒤집어진 리스트: " + str(numbers))