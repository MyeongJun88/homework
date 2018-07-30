from random import randint

Num_Tries = 4
Answer=randint(1,20)

tries = 0
guess = -1

while tries < Num_Tries and guess != Answer:
   guess = int(input("기회가 %d번 남았습니다. 1-20 사이의 숫자를 맞춰보세요: " % (Num_Tries - tries)))
   tries = tries + 1

   if Answer > guess:
    print("Up")
   elif Answer < guess:
    print("Down")

if Answer == guess:
    print("축하합니다. %d번만에 숫자를 맞추셨습니다." % (tries))
else:
    print ("아쉽습니다. 정답은 %d였습니다." % (Answer))

