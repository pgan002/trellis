#!/usr/bin/python3
import argparse
import math
import sys

import large_int


UNITS_AND_TEENS = [
    'zero',
    'one',
    'two',
    'three',
    'four',
    'five',
    'six',
    'seven',
    'eight',
    'nine',
    'ten',
    'eleven',
    'twelve',
    'thirteen',
    'fourteen',
    'fifteen',
    'sixteen',
    'seventeen',
    'eighteen',
    'nineteen'
]
TENS = [
    'ten',
    'twenty',
    'thirty',
    'forty',
    'fifty',
    'sixty',
    'seventy',
    'eighty',
    'ninety'
]
POWERS = {
    1: '',
    2: 'hundred',
    3: 'thousand'
}
SEPARATORS = {1: '-', 2: ' and'}


def int_to_words(n):
    """Convert integer `n` to words in English"""
    if not isinstance(n, (int, str)):
        raise ValueError('Expected an integer')
    n = int(n)

    sign = 'minus ' if n < 0 else ''
    n = abs(n)

    if n > 10**(large_int.MAX):
        raise ValueError('Error: %s: Maximum absolute number is 10**%s-1' 
                         % (n, large_int.MAX))

    # Units and teens
    if n <= 19:
        return sign + UNITS_AND_TEENS[n]
    
    # Tens
    if n <= 99:
        quotient, remainder = divmod(n, 10)
        if remainder:
            suffix = '-' + UNITS_AND_TEENS[remainder]
        else:
            suffix = ''
        return sign + TENS[quotient-1] + suffix
    
    # Hundreds, thousands and greater
    exponent = int(math.log(n + 0.1, 10))  # Add 0.1 to avoid rounding error
    if exponent < 6:
        exponent = min(exponent, 3)
        quotient, remainder = divmod(n, 10**exponent)
    else:
        quotient, remainder = divmod(n, 10**(exponent // 3 * 3))

    unit = POWERS.get(exponent, large_int.large_int_word(exponent // 3 - 1))
    prefix = sign + int_to_words(quotient) + ' ' + unit
    if remainder:
        return prefix + SEPARATORS.get(exponent, '') + ' ' + int_to_words(remainder)
    else:
        return prefix


parser = argparse.ArgumentParser(
    description='Convert an integer number into words in English.\n'
    'The largest number is 10**%s-1. '
    'For large numbers, use the short scale used in US, Canada, and modern '
    'British English.' % large_int.MAX
)
parser.add_argument('integer', nargs='*', type=int)


if __name__ == '__main__':
    args = parser.parse_args()
    for n in args.integer:
        try:
            print(int_to_words(n))
        except ValueError as e:
            print(e, file=sys.stderr)

# Test:
# 12 'twelve'
# 20 'twenty'
# 99 'ninety-nine'
# 101 'one hundred and one'
# 1001 ' one thousand and one'
# 10093 'ten thousand and ninety-three'
# 1234 'one thousand two hundred and thirty-four'
# 12345 'twelve thousand three hundred and forty-five'
# 100000000 'ten million'
# 0 'zero'
# -10 'minus ten'
# 'hello' Error
# 1.0 Error

