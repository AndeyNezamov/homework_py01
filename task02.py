# 3. Напишите код, который запрашивает число и сообщает является ли оно простым
# или составным. Используйте правило для проверки: “Число является простым, если
# делится нацело только на единицу и на себя”. Сделайте ограничение на ввод
# отрицательных чисел и чисел больше 100 тысяч.
def limiter():
    while True:
        number = int(input('Введите число: '))
        if 100000 > number > 0:
            break
        else:
            continue
    return number


def composite_number(func):
    count = 0
    for i in range(1, func+1):
        if func % i == 0:
            count += 1
    if count < 2:
        result = 'Единица не является ни простым не состовным числом'
    elif count == 2:
        result = 'Число простое'
    else:
        result = 'Число составное'
    return result


print(composite_number(limiter()))
