#!/usr/bin/python3
import sys

# Reference: https://en.wikipedia.org/wiki/Names_of_large_numbers


UNITS = [
    '', 'mi', 'bi', 'tri', 'quadri', 'quinti', 'sexti', 'septi', 'octi', 'noni',
    'deci',
]
UNIT_PREFIXES = [
    '', 'un', 'duo', 'tre', 'quattuor', 'quinqua', 'se', 'septen', 'octo', 
    'noven'
]
TENS = [
    '', 'vi', 'tri', 'quadra', 'quinqua', 'sexa', 'septua', 'octo', 'nona'
]
HUNDREDS = [
    'centi', 'ducenti', 'trecenti', 'quadringenti', 'quingenti', 'sescenti', 
    'septigenti', 'octigenti', 'nongenti'
]
MAX = (1000 * 3) + 1


def _teen(ix):
    quotient, remainder = divmod(ix, 10)
    prefix = UNIT_PREFIXES[remainder]
    if not quotient:
        suffix = ''
    else:
        assert quotient == 1
        suffix = 'deci'
    return prefix + suffix


def large_int_word(ix):
    if ix <= 10:
        word = UNITS[ix]
    elif ix < 20:
        word = _teen(ix)
    elif ix < 100:
        quotient, remainder = divmod(ix, 10)
        suffix = TENS[quotient - 1] + 'gint'
        prefix = UNIT_PREFIXES[remainder]
        word = prefix + suffix
    elif ix < 1000:
        quotient, remainder = divmod(ix, 100)
        suffix = HUNDREDS[quotient - 1]
        if remainder:
            prefix = _teen(remainder)
        else:
            prefix = ''
        word = prefix + suffix
    elif ix == 1000:
        word = 'millini'
    return word + 'llion'


if __name__ == '__main__':
    print(large_int_word(int(sys.argv[1])))
