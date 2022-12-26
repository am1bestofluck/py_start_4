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
from subfunctions import split_number




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


def t2() -> list[int]:
    return


def t3() -> set(Any):
    return


def t4() -> None:
    return


def t5() -> None:
    return


def main():
    return


if __name__ == "__main__":
    main()
