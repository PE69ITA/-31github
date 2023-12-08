def sum_of_elements(lst):
    """
    Функция для вычисления суммы всех элементов в списке.

    :param lst: Список чисел.
    :return: Сумма всех элементов в списке.
    """
    total = 0
    for num in lst:
        total += num
    return total

# Пример использования:
my_list = [1, 2, 3, 4, 5]
result = sum_of_elements(my_list)
print(f"Сумма элементов списка {my_list}: {result}")
