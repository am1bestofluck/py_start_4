

import math
import os
import random
import re
import sys
from copy import deepcopy
from string import ascii_letters, whitespace, digits
from typing import List
# import pdb


def split_number(number: float) -> List:
    """разбиваем число"""
    positive = number > 0
    whole_part = int(number)
    fractial_part = (number - math.floor(number) if positive
                     else number - math.ceil(number))
    return [whole_part, fractial_part]


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


def write_polynomial(max_pow: int) -> str:
    """формируем многочлен"""
    multiplicators = range(100)
    masks_obligatory = 'abc'
    masks_optional = ['d', 'e', 'f', '']
    operators = '+-'
    sign_optional = ['', '-']
    pow_obligatory = [f'**{i}' for i in range
                      (min(2, max_pow), max(2, max_pow))]
    if pow_obligatory == []:
        pow_obligatory = [f'**{i}' for i in range
                          (min(2, max_pow+1), max(2, max_pow+1))]

    pow_optional = deepcopy(pow_obligatory)
    pow_optional += ''
    output = (random.choice(sign_optional) + str(random.choice(multiplicators))
              + random.choice(masks_obligatory) + random.choice(pow_obligatory)
              + random.choice(masks_optional)

              + f' {random.choice(operators)} '

              + random.choice(sign_optional) +
              str(random.choice(multiplicators))
              + random.choice(masks_obligatory) + random.choice(masks_optional)

              + f' {random.choice(operators)} '

              + random.choice(sign_optional) +
              str(random.choice(multiplicators))
              )
    white_spaces = re.compile("[' ']*")
    output = re.sub(pattern=white_spaces, repl='', string=output)
    fix_substract = re.compile('\+\-')
    output = re.sub(pattern=fix_substract, repl='-', string=output)
    fix_substract = re.compile('\-\+')
    output = re.sub(pattern=fix_substract, repl='-', string=output)
    fix_add = re.compile('\+\+')
    output = re.sub(pattern=fix_add, repl='+', string=output)
    fix_add = re.compile('\-\-')
    output = re.sub(pattern=fix_add, repl='+', string=output)
    fix_pow_0 = re.compile(f'[{ascii_letters}]*\*\*0')
    output = re.sub(pattern=fix_pow_0, repl='', string=output)
    return output


def merge_polynomial(expression_i: str) -> str:
    """Пробуем сократить выражение"""
    # получилось
    expression_m = expression_i
    fix_substract = re.compile('\+\-')
    expression_m = re.sub(pattern=fix_substract, repl='-', string=expression_m)
    fix_substract = re.compile('\-\+')
    expression_m = re.sub(pattern=fix_substract, repl='-', string=expression_m)
    expression_m = expression_m.replace('+', ' +').replace('-', ' -')
    lst = re.split(' ', expression_m)
    while '' in lst:
        lst.remove('')
    pairs = {'': 0}  # raw numbers
    for member in lst:
        try:
            pairs[''] += int(member)
        except ValueError:
            index = 0
            while member[index] in '0123456789+- ':
                index += 1
            if member[index:] in pairs:
                pairs[member[index:]] += int(member[:index])
            else:
                pairs[member[index:]] = int(member[:index])
    expression_o = ''
    for i in pairs:
        expression_o += f'{"+" if pairs[i]>0 else ""}{str(pairs[i])}{str(i)}'
    expression_o = expression_o.removeprefix('+')
    return expression_o
