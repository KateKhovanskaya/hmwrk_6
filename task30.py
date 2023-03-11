# Задача 30:  Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки

# pytest -v tests\test_30.py

def arithmetic_progression(first: int,
                           diff: int,
                           quantity: int) -> list[int]:
    """Возвращает список арифметической прогрессии по заданным:
    1) первый элемент
    2) разность
    3) количество элементов"""

    rez_list = list()
    for i in range(1, quantity+1):
        rez_list.append(first + (i-1) * diff)
    return rez_list


first = int(input("Введите стартовое число: "))
diff = int(input("Введите разность прогрессии: "))
quantity = int(input("Введите количество членов прогрессии: "))
print(arithmetic_progression(first, diff, quantity))