import random

# Шаг 1: Переворот списка
def reverse_list(lst):
    """Шаг 1: Функция принимает на вход список и возвращает перевёрнутый список."""
    return lst[::-1]

# Шаг 2: Изменение значений списка
def modify_list(lst, new_values=None):
    """
    Шаг 2: Функция принимает на вход список и изменяет одно, несколько или все значения списка.
    Возвращает изменённый список.
    """
    if new_values:
        for i, val in enumerate(new_values):
            if i < len(lst):
                lst[i] = val
    return lst

# Шаг 3: Сравнение списков
def compare_lists(*lists):
    """Шаг 3: Функция принимает два или более списков и сравнивает их. Возвращает отметку о равенстве."""
    return all(lst == lists[0] for lst in lists)

# Шаг 4: Выбор диапазона значений из списка
def select_range(lst, start=0, end=None, step=1):
    """
    Шаг 4: Функция принимает на вход список и дополнительные параметры (start, end, step).
    Возвращает список, соответствующий диапазону.
    """
    end = end if end is not None else len(lst)
    return lst[start:end:step]

# Шаг 5: Создание списка на основе параметров
def create_list(*values):
    """Шаг 5: Функция принимает на вход параметры и создаёт список, возвращая его."""
    return list(values)

# Шаг 6: Вставка элемента в заданную позицию списка
def insert_into_list(lst, index, value):
    """Шаг 6: Функция вставляет элемент в заданную позицию списка."""
    lst.insert(index, value)
    return lst

# Шаг 7: Объединение и сортировка списков
def merge_and_sort(*lists, reverse=False):
    """Шаг 7: Функция объединяет все переданные списки и сортирует их."""
    merged_list = sum(lists, [])
    return sorted(merged_list, reverse=reverse)

# Шаг 8: Создание случайного списка и проверка длины
def create_random_list():
    """Шаг 8: Функция создаёт список случайной длины и проверяет его чётность."""
    lst = [random.randint(0, 100) for _ in range(random.randint(5, 15))]
    while len(lst) % 2 == 0:
        print(f"List {lst} is even-length. Creating a new list...")
        lst = [random.randint(0, 100) for _ in range(random.randint(5, 15))]
    print(f"Odd-length list: {lst}")
    central_element = lst[len(lst) // 2]
    count = lst.count(central_element)
    print(f"Central element {central_element} appears {count} time(s).")
    return lst

# Шаг 9: Прибавление списков с учётом порога
def append_with_threshold(lst, *others, threshold=10):
    """Шаг 9: Функция прибавляет к первому списку другие списки с учётом порога."""
    lst.extend(sum(others, []))
    if len(lst) > threshold:
        lst = lst[:threshold]
    return lst

# Шаг 10: Сортировка списков
def sort_list_by_length(lst):
    """Сортировка по длине элементов (для строк или вложенных списков)."""
    return sorted(lst, key=len)

def sort_list_by_sum(lst):
    """Сортировка списка по сумме элементов."""
    return sorted(lst, key=sum)

def sort_list_alphabetically(lst):
    """Сортировка строкового списка в алфавитном порядке."""
    return sorted(lst)

def sort_with_map(lst):
    """Сортировка списка по числовому значению с использованием map()."""
    return list(map(int, sorted(map(str, lst))))

def sort_and_double(lst):
    """Удвоение чисел в списке с использованием map()."""
    return list(map(lambda x: x * 2, lst))

def sort_and_square(lst):
    """Возведение чисел в квадрат с использованием map()."""
    return list(map(lambda x: x ** 2, lst))

# Шаг 11: Извлечение минимального элемента
def extract_min(lst):
    """Шаг 11: Функция извлекает и удаляет минимальный элемент списка."""
    if not lst:
        return None
    min_val = min(lst)
    lst.remove(min_val)
    return min_val

# Шаг 12: Операции над кортежами
def sum_tuples(*tuples):
    """Суммирует элементы всех кортежей."""
    return tuple(sum(values) for values in zip(*tuples))

def multiply_tuples(*tuples):
    """Умножает элементы всех кортежей."""
    result = []
    for values in zip(*tuples):
        product = 1
        for val in values:
            product *= val
        result.append(product)
    return tuple(result)

# Шаг 13: Получение типов данных элементов кортежа
def tuple_element_types(*args):
    """Возвращает кортеж из типов данных элементов входного кортежа."""
    return tuple(type(arg) for arg in args)

# Шаг 14: Проверка на наличие элемента в кортеже
def is_element_in_tuple(tpl, element):
    """Проверяет наличие элемента в кортеже."""
    return element in tpl

# Шаг 15: Формирование двумерного списка
def create_2d_list(*lists):
    """Формирует двумерный список на основе входных списков."""
    return [list(sublist) for sublist in lists]

# Шаг 16: Операции над словарями
def get_dict_keys(dct):
    """Возвращает список ключей словаря."""
    return list(dct.keys())

def get_dict_values(dct):
    """Возвращает список значений словаря."""
    return list(dct.values())

def remove_dict_key(dct, key):
    """Удаляет ключ из словаря (если есть) и возвращает обновлённый словарь."""
    dct.pop(key, None)
    return dct

# Шаг 17: Подсчёт встречаемости ключей в словарях
def count_key_occurrences(key, *dicts):
    """Считает, сколько раз ключ встречается во всех словарях."""
    return sum(1 for dct in dicts if key in dct)

# Шаг 18: Поиск элемента в сложном словаре
def find_deep_element(dct, key):
    """Ищет элемент на последнем уровне вложенности в сложном словаре."""
    if isinstance(dct, dict):
        for k, v in dct.items():
            if k == key:
                return v
            elif isinstance(v, dict):
                result = find_deep_element(v, key)
                if result is not None:
                    return result
    return None
