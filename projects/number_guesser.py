import random


def is_valid(n):
    return n.isdigit() and 1 < int(n) < 101


print('Добро пожаловать в числовую угадайку')
magic_number = random.randint(1, 101)
count = 0
while True:
    num = input('Угадай число:')
    if not is_valid(num):
        print('А может быть все-таки введем целое число от 1 до 100?')
        continue
    num = int(num)
    if num < magic_number:
        print('Ваше число меньше загаданного, попробуйте еще разок')
        count += 1
    elif num > magic_number:
        print('Ваше число больше загаданного, попробуйте еще разок')
        count += 1
    else:
        print(f'Вы угадали, поздравляем! Было {count} попыток')
        print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
        break
