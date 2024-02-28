import random

count = 0
user_choose = 0
computer_choose = random.randint(1, 100)

while user_choose != computer_choose:
    user_choose = int(input("1부터 100 사이의 숫자를 넣어주세요 : "))

    # print(f"\n 너는 {user_choose}, 컴퓨터는 {computer_choose}.\n")
    # 컴퓨터가 고른 숫자 확인용 코드

    if (user_choose < 1 or user_choose > 100):
        print("유효한 범위가 아닙니다. 1부터 100까지의 숫자를 입력해주세요.\n")
        continue

    if (user_choose == computer_choose):
        print(f"정답입니다! {count}회 만에 맞췄어요!\n다시 플레이하시겠어요? (예/아니오) : ")
        user_answer = input()

        if (user_answer != '예' and user_answer != '아니오'):
            print("예 또는 아니오 중에 입력해주세요 : ")
            user_answer = input()

        if (user_answer == "예"):
            print(f"\n게임을 다시 시작합니다.\n이전 게임 최고 시도 횟수 :{count}")
            count = 0
            computer_choose = random.randint(1, 100)
            continue
        else:
            print("게임을 종료합니다.\n")
            break

    elif (user_choose > computer_choose):
        count += 1
        print("DOWN")
    else:
        count += 1
        print("UP")
