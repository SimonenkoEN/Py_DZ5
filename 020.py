# ДЗ к семинару 4, задание 3
# Создайте функцию генератор чисел Фибоначчи


def fibonacci(n):
    fn1 = 0
    fn2 = 1
    for i in range(n + 1):
        if i == 0:
            yield 0
        elif i == 1:
            yield 1
        else:
            fn = fn1 + fn2
            fn1, fn2 = fn2, fn
            yield fn

if __name__ == '__main__':
    num = int(input('Введите целое число: '))

    for _, i in enumerate(fibonacci(num)):
        print(i, end='  ')