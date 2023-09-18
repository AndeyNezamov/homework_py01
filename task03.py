from random import randint

number = randint(0, 1000)
print(number)
count = 0
while count < 10:
    user_number = int(input('Введите число: '))
    if user_number > number:
        print('Ваше число больше загаданного')
        count += 1
    elif user_number < number:
        print('Ваше число меньше загаданного')
        count += 1
    else:
        print('Угадал')
        break

if count == 10:
    print('Вы проиграли')
