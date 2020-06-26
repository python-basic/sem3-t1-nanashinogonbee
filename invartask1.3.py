import math

a, b, c = [int(input('{}: '.format(chr(i + 97)))) for i in range(3)]
print(a, b, c)

try:
    p = sum((a, b, c)) / 2
    S = math.sqrt(p * (p - a) * (p - b) * (p - c))
except (ValueError, TypeError) as e:
    S = e

print('S = {}'.format(S))

