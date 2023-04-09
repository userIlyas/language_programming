# number 2
from random import randint
numbers = []
for i in range(7):
    s = ""
    for j in range(7):
        s += str(randint(0, 9))
    numbers.append(s)
for g in range(len(numbers)):
    print(f"Номер элемента: {g}. Число: {numbers[g]} ")


# number 3
data = []
for i in range(1, 13):
    s = float(input(f"Введите количество осадков в {i} месяце: "))
    data.append(s)
print(f"Суммарное годовое количество осадков {sum(data)}")
print(f"Среднее годовое количество осадков {sum(data)/12}")
print(f"Самый осадочный месяц {data.index(max(data))+1}")
print(f"Самый НЕосадочный месяц {data.index(min(data))+1}")