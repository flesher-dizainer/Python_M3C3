# взведение числа в степень
def task_1():
    try:
        x = int(input('Enter x number value: '))
        y = int(input('Enter y number value: '))
        result = 1
        for i in range(y):
            result *= x
        print(f'{x} ** {y} = {result}')
    except ValueError:
        print('Error input value')


# Подсчитать количество целых чисел в диапазоне от
# 100 до 999 у которых есть две одинаковые цифры
def task_2():
    counter_value = 0
    for i in range(100, 1000):
        str_value = str(i)
        for s in str_value:
            if str_value.count(s) > 1:
                counter_value += 1
                break
    print(counter_value)


# Подсчитать количество целых чисел в диапазоне от
# 100 до 9999 у которых все цифры разные
def task_3():
    counter_value = 0
    for i in range(100, 10000):
        str_value = str(i)
        count_value = 0
        for s in str_value:
            if str_value.count(s) > 1:
                count_value += 1
                break
        if count_value == 0:
            counter_value += 1
    print(counter_value)


# Пользователь вводит любое целое число.
# Необходимо из этого целого числа удалить все цифры 3 и 6 и вывести обратно на экран.
def task_4():
    try:
        input_value = int(input('Enter number value: '))
        result = ''
        for i in str(input_value):
            if (i != '3') and (i != '6'):
                result += i
        print(result)
    except ValueError:
        print('Error input value')

    
if __name__ == '__main__':
    task_1()
    task_2()
    task_3()
    task_4()
