#intro -> 반복문
#가위바위보 메소드 -> if조건문
# 승, 무, 패 저장 -> dict
# print input
import random


def gamestart():
    while True:

#gamestart() -> 실행 시
# print_intro() -> print해주기
# get_user_input() -> 실행 시 return input /str
# calc_result()-> 실행하게 되면 return key -> value(win, draw, lost) +=1
# print_result() -> 실행시 return print()

def gamestart():
    print_intro()
    user = get_user_input()
    com = random.randint(1,3)
    result = calc_result(???)
    print_result(result)

def print_intro():
    input_msg = '1, 가위, 2, 바위, 3, 보, (종료 : q,Q)'
    print(input_msg)

def get_user_input():
    intro_str = """가위 바위 보 게임!!! 
    반가워요
    """


def calc_result(user, com):
    if user == com:
        result = "draw"
    elif user % 3 + 1 == com:
        result = "lost"
    elif com % 3 + 1 == com:
        result = "win" \
    return result

def print_result(result):
    if result == "win:"
    print("이겼습니다")
    elif result == "lost"
    print("졌습니다")
    else:
    print("비겼습니다")

gamestart()


score_msg = "승 : {win}, 패 {lost}, 비김: {draw}"

while True:
    print(intro_str)
    while True:
        input_str = input(input_msg)
        if input_str in ["1","2","3","q","Q"]:
            if input_str in["q", "Q"]:
                print("종료하겠습니다")
                exit()
            else:
                user = int(input_str)
                com = random.randint(1,3)
        if user == com:
            print("비겼습니다")
            score['draw'] += 1
        elif user % 3 + 1 == com:
            print("졌습니다")
            score['lost'] += 1
        elif com % 3 + 1 == com:
            print("이겼습니다")
            score['win'] += 1
        print(score_msg.format(

            win=score['win'],
            draw=score['draw'],
            lost=score['lost']
        ))
        else :
            print("잘못골랐습니다 다시 입력해주세요")




score = {'win' : 0, 'draw': 0, 'lost':0}
rsp_set = ["가위", "바위", "보"]

input_str = input("무엇을 내시겠습니까?")
#input_str =="q, Q"-> 게임을 종료

user = int(input_str)
com = random.randint(1,3)





