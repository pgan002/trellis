#!/usr/bin/python3
import argparse
import math
import sys

# Reference: https://en.wikipedia.org/wiki/Names_of_large_numbers

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
POWERS = [
        'thousand',
        'million',
        'billion',
        'trillion',
        'quadrillion',
        'quintillion',
        'sextillion',
        'septillion',
        'octillion',
        'nonillion',
        'decillion',
        'undecillion',
        'duodecillion',
        'tredecillion',
        'quattuordecillion',
        'quindecillion',
        'sexdecillion',
        'septendecillion',
        'octodecillion',
        'novemdecillion',
        'vigintillion',
        'unvigintillion',
        'duovigintillion',
        'tresvigintillion',
        'quattuorvigintillion',
        'quinquavigintillion',
        'sesvigintillion',
        'septemvigintillion',
        'octovigintillion',
        'novemvigintillion',
        'trigintillion',
]

MAX_EXPONENT = 3 * (1 + len(POWERS))


def int_to_words(n):
    """Convert integer `n` to words in English"""
    if not isinstance(n, (int, str)):
        raise ValueError('Expected an integer')
    n = int(n)

    sign = 'minus ' if n < 0 else ''
    n = abs(n)
    
    if n > 10**(3*(1+len(POWERS))):
        raise ValueError('Error: %s: Maximum absolute number is 10**%s-1' 
                         % (n, MAX_EXPONENT))

    # Units and teens
    if n <= 19:
        return sign + UNITS_AND_TEENS[n]
    
    # Tens
    if n <= 99:
        tens, units = divmod(n, 10)
        prefix = sign + TENS[tens - 1]
        if not units:
            return prefix
        else:
            return prefix + '-' + UNITS_AND_TEENS[units]

    # Hundreds
    if n <= 999:
        quotient, remainder = divmod(n, 100)
        prefix = sign + int_to_words(quotient) + ' hundred'
        if not remainder:
            return prefix
        else:
            return prefix + ' and ' + int_to_words(remainder)

    # Other
    exponent = int(math.log(n + 0.1, 10))  # Add 0.1 to avoid rounding error
    quotient, remainder = divmod(n, 10**exponent)
    prefix = sign + int_to_words(quotient) + ' ' + POWERS[exponent // 3 - 1]
    if not remainder:
        return prefix
    if remainder <= 99:
        prefix += ' and'
    return prefix + ' ' + int_to_words(remainder)


parser = argparse.ArgumentParser(
    description='Convert an integer number into words in English.\n'
    'The largest number is 10**%s-1. '
    'For large numbers, use the short scale used in US, Canada, and modern '
    'British English.' % MAX_EXPONENT
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
12
20
99
101
1001
10093
1234
12345
0
-10
'hello'
1.0
10**64
