

from typing import List, Any
import math

def split_number(number: float) -> List:
    """разбиваем число"""
    positive = number > 0
    whole_part = int(number)
    fractial_part= (number - math.floor(number) if positive
            else number - math.ceil(number))
    return [whole_part,fractial_part]
