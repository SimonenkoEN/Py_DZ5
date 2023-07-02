# ДЗ к семинару 5, задание 2
# Напишите однострочный генератор словаря, который принимает
# на вход три списка одинаковой длины: имена str, ставка int,
# премия str с указанием процентов вида «10.25%». В результате
# получаем словарь с именем в качестве ключа и суммой
# премии в качестве значения. Сумма рассчитывается
# как ставка умноженная на процент премии

if __name__ == '__main__':
    name = ['Иванов', 'Петров', 'Кузнецов', 'Сидоров']
    salary = [1000, 1000, 1500, 2000]
    percent = ['5%', '10%', '10%', '10%']

    awards_dict = {name[i] : salary[i] * int(percent[i][:-1]) / 100 for i in range(len(name))}
    print(awards_dict)
