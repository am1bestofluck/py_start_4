


import math
import os
import sys
from typing import List, Any

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
        except ValueError:
            pass
        # закругляемся без шума
        except KeyboardInterrupt:
            sys.exit()
        except EOFError:
            sys.exit()
    return invite


def input_int(invite: str = 'input int') -> int:
    while not isinstance(invite, int):
        try:
            invite = int(input(invite))
        except ValueError:
            pass
        # закругляемся без шума
        except KeyboardInterrupt:
            sys.exit()
        except EOFError:
            sys.exit()
    return invite


def Break() -> None:
    """Чистим консоль, чтобы не переполнять внимание :'D.  """
    input("Enter to proceed.")
    os.system('cls')
    return None