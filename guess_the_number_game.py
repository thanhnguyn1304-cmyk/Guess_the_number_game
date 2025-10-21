import random

number = random.randint(1, 100)

print('The number is between 1 and 100')

closest_answer = 100

while True :
    try:
        player = int(input("What's your guess ?: "))

        if abs(player-number) < abs(closest_answer-number):
            closest_answer = player
        if player > number:
            print(f'Lower! The closest answer was: {closest_answer}')
        elif player < number:
            print(f'Higher! The closest answer was: {closest_answer}')
        else:
            print("That's the correct answer!")
            break
    except ValueError:
        print('Invalid answer, please choose again! ')
        continue


