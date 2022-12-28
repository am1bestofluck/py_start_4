

import math
import os
import random
import re
import sys
from copy import deepcopy
from string import ascii_letters, whitespace, digits
from typing import List
import pdb


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
    multiplicators = range(100)
    masks_obligatory = 'abc'
    masks_optional = ['d','e','f','']
    operators = '+-'
    sign_optional = ['', '-']
    pow_obligatory = [f'**{i}' for i in range
                        (min(2,max_pow),max(2,max_pow)) ]
    if pow_obligatory ==[]:
        pow_obligatory = [f'**{i}' for i in range
                        (min(2,max_pow+1),max(2,max_pow+1)) ]

    pow_optional = deepcopy(pow_obligatory)
    pow_optional += ''
    output = (random.choice(sign_optional) + str(random.choice(multiplicators))
            + random.choice(masks_obligatory) + random.choice(pow_obligatory) 
            + random.choice(masks_optional)

            + f' {random.choice(operators)} '
            
            + random.choice(sign_optional) + str(random.choice(multiplicators))
            + random.choice(masks_obligatory) + random.choice(masks_optional)

            + f' {random.choice(operators)} '

            + random.choice(sign_optional) + str(random.choice(multiplicators))
            )
    white_spaces = re.compile("[' ']*")
    output = re.sub(pattern=white_spaces, repl='' ,string=output)
    fix_substract = re.compile('\+\-')
    output = re.sub(pattern=fix_substract, repl='-' ,string=output)
    fix_substract = re.compile('\-\+')
    output = re.sub(pattern=fix_substract, repl='-' ,string=output)
    fix_add = re.compile('\+\+')
    output = re.sub(pattern=fix_add, repl='+' ,string=output)
    fix_add = re.compile('\-\-')
    output = re.sub(pattern=fix_add, repl='+' ,string=output)
    fix_pow_0=re.compile(f'[{ascii_letters}]*\*\*0')
    output = re.sub(pattern=fix_pow_0,repl='',string=output)
    adress_zero = re.compile(f'[\+\-]0[{ascii_letters}\*]*')
    return output


def merge_polynomial(expression_i:str) -> str:
    """Пробуем сократить выражение"""
    expression_o = expression_i
    fix_substract = re.compile('\+\-')
    expression_o = re.sub(pattern=fix_substract, repl='-' ,string=expression_o)
    fix_substract = re.compile('\-\+')
    expression_o = re.sub(pattern=fix_substract, repl='-' ,string=expression_o)
    expression_o = expression_o.replace('+', ' +').replace('-',' -')
    # raw_numbers = re.compile('[\+\-]?[0-9]+[^a-zA-Z]')
    lst = re.split('[\+\-]',expression_o)
    sum_of_raw_digits = 0
    index = 0
    while index > len(lst):
        try:
            if isinstance(int,int(lst[index])):
                sum_of_raw_digits += int(lst[index])

merge_polynomial("35a**2e +64ae -61 +24c**3e +83b -17")
