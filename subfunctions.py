

from typing import List, Any
import math

def split_number(number: float) -> List:
    """разбиваем число"""
    positive = number > 0
    whole_part = int(number)
    fractial_part= (number - math.floor(number) if positive
        else number - math.ceil(number))
    return [whole_part,fractial_part]


def input_float(invite: str = 'input float') -> float:
    while not isinstance(invite, float):
        try:
            invite = float(input(invite))
        except:
            pass
    return invite


def input