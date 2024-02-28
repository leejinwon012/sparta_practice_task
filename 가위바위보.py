import random

win = 0
lose = 0
draw = 0

user_choose = input("선택하세요 (가위, 바위, 보) : ")
possible_choose = ("가위", "바위", "보")
computer_choose = random.choice(possible_choose)

while (True):
    # 부적절한 입력
    if (user_choose not in possible_choose):
        print("유효한 입력값이 아닙니다. 가위, 바위, 보 중에 입력해주세요 : ")
        user_choose = input()
        continue
    # print(f"너는 {user_choose}, 컴퓨터는 {computer_choose}.\n")
    # 컴퓨터가 고른 선택 확인용 코드

    # 무
    if user_choose == computer_choose:
        print(f"둘 다 {user_choose}를 선택했습니다. 비겼습니다!\n")
        draw += 1

    # 승/패
    if user_choose == "바위":
        if computer_choose == "가위":
            print("당신이 이겼습니다!\n")
            win += 1
        else:
            print("당신은 졌습니다.\n")
            lose += 1

    elif user_choose == "보":
        if computer_choose == "바위":
            print("당신이 이겼습니다!\n")
            win += 1
        else:
            print("당신은 졌습니다.\n")
            lose += 1

    elif user_choose == "가위":
        if computer_choose == "보":
            print("당신이 이겼습니다.\n")
            win += 1
        else:
            print("당신은 졌습니다.\n")
            lose += 1

    # 게임 재참여 의사
    re_game = input("한번 더 할래? (y/n): ")

    # while문의 while break를 위한 변수
    flag = 0

    while (True):
        if re_game.lower() == "y":
            computer_choose = random.choice(possible_choose)
            user_choose = input("선택하세요 (가위, 바위, 보): ")
            break

        elif re_game.lower() == "n":
            print("게임을 종료합니다")
            print(f"승 : {win}\n패 : {lose}\n무승부 : {draw}")
            flag = 1
            break
        # 부적절한 입력
        else:
            print("y 또는 n 중에 입력해주세요: ")
            re_game = input()

    # while문의 while문을 위한 break
    if flag:
        break
