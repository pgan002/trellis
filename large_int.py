#!/usr/bin/python3
import sys

# Reference: https://en.wikipedia.org/wiki/Names_of_large_numbers


UNITS = [
    '', 'mi', 'bi', 'tri', 'quadri', 'quinti', 'sexti', 'septi', 'octi', 'noni'
]
UNIT_PREFIXES = [
    '', 'un', 'duo', 'tre', 'quattuor', 'quinqua', 'se', 'septen', 'octo', 
    'noven'
]
TENS = [
    '', 'deci', 'viginti', 'triginti', 'quadraginti', 'quinquaginti', 
    'sexaginti', 'septuaginti', 'octogingi', 'nonaginti'
]
HUNDREDS = [
    '', 'centi', 'ducenti', 'trecenti', 'quadringenti', 'quingenti', 'sescenti', 
    'septigenti', 'octigenti', 'nongenti'
]
MAX = 3 * 10000 + 3


def large_int_word2(x):
    """Return the name of the large integer n = 10 ** (3 * x + 3)"""

    digits = [int(i) for i in x]
    units = tens = hundreds = thousands = ''

    if len(digits) == 1:
        units = UNITS[digits(-1)]
    else:
        units = UNIT_PREFIXES[digits[-1]]
        tens = TENS[digits[-2]]
        if len(digits) >= 3:
            hundreds = HUNDREDS[digits[-3]]
        if len(digits) >= 4:
            thousands = UNITS[digits[-4]] + 'llini'
        if len(digits) >= 5:
            raise

    return units + tens + hundreds + thousands + 'llion'


if __name__ == '__main__':
    print(large_int_word2(sys.argv[1]))
