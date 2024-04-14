import random
for i in range(10) :
    random_number = random.randint(1, 100)
    print(i, ":", random_number)

game_count = 1

while True :
    my_number = int(input("1~100까지의 숫자를 입력하세요"))

    if my_number > random_number :
        print("다운")
    elif my_number < random_number :
        print("업")
    elif my_number == random_number :
        print(f"축하합니다, {game_count} 안에 맞췄습니다")
        break

    game_count = game_count + 1

