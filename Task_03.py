# Задача 3
# Вывести по номеру месяца кол-во дней в нем (без указания названия месяца, в феврале 28 дней)
# Результат проверки вывести на консоль
# Если номер месяца некорректен - сообщить об этом

user_input = input("Введите номер месяца: ")
month = int(user_input)
print('Вы ввели', month)
days=[31,28,31,30,31,30,31,31,30,31,30,31]
if not 0 < month<= 12:
    print("Не правильно выбран месяц!")
    quit()
print(days[month -1])

# Идею понял. Хорошо
# есть ещё такие варианты

# Решение 1
if month in [1, 3, 5, 7, 8, 10, 12]:
    print(31)
elif month in [4, 6, 9, 11]:
    print(30)
elif month == 2:
    print(28)
else:
    print('Введен неправильный номер месяца!')

# Решение 2
import calendar as cl  # используем модуль для получения функции

year_input = input("Введите год: ")
month_input = input("Введите номер месяца: ")

year = int(year_input)
month_ = int(month_input)
print(cl.monthrange(year, month_))
