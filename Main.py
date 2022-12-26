""" t1: Вычислить периодическое число с заданной точностью.  

t2: Разбить число на простые множители.  

t3: Вывести уникальные значения заданного списка.

t4: Дана предельная натуральная степень многочлена. 
Придумать всё остальное и записать в файл.

t5: Даны два файла содержащих запись многочлена. 
Сложить их и записать в третий файл.
"""

from __future__ import annotations


__version__ = "#4"
__author__ = "anton6733@gmail.com"


# standart imports
from math import pi
from typing import Any

# local imports
from subfunctions import (Break, split_number,input_float, input_int)




def t1(number_i: int | float, round_to: int) -> float:
    """переизобретаем round

    number -  число к округлению

    round_to - ожидаемое количество разрядов в выводе 
    """
    """
    parts - разбиваем целую и округляемую часть
    number_m - изменяемая (дробная) часть числа
    fractial_stringified - работаем с числом как со строкой... 
    """

    # шутка в том что получилось точнее чем в round, например:
    # assert round(10.987654321, 3) == t1( 10.987654321, 3) - 
    # round даёт последним знаком 8 а не 7. Воот :].

    # в принципе можно потом, если время останется, попробовать приобщить
    # decimal
    parts = split_number(number_i)
    number_m = parts[1]
    fractial_stringified = str(number_m)[2:]
    round_to = len(fractial_stringified) if (
        abs(round_to) > len(fractial_stringified)) else round_to
    number_m = 0 if round_to == 0 else (int(fractial_stringified[:abs(round_to)])
                                        * 10 ** -abs(round_to))

    return parts[0] + number_m


def t2(number: int) -> list[int]:
    """Раскладываем число на простые множители"""
    """
    output - вывод
    number_m - дублируем входящую переменную на всякий случай  
    is_composite - условие выхода из цикла; выходим если число 
    оказалось простым

    """
    output = []
    number_m = number
    is_composite=True
    while is_composite:
        if number_m == 1:
            break
        for try_divide in range( 2, number_m+1,1):
            if not number_m%try_divide:
                output.append(try_divide)
                number_m = int(number_m /try_divide)
                break
    return output


def t3() -> set(Any):
    return


def t4() -> None:
    return


def t5() -> None:
    return


def main() -> None:
    """Сценарий, в этот раз без консоли"""
    # print(t1.__doc__)
    # print(t1(
    #     input_float("Input number to reduce"), 
    #     input_int("Input expected fractional length")))
    # Break()
    print(t2.__doc__)
    print(t2(input_int("Number to factorize ")))
    # Break()
    return None


if __name__ == "__main__":
    main()
