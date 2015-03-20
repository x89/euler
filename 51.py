# Project Euler #51. The last remaining euler to do < #60

from math import sqrt, ceil

n = 10000000

ps = [1 for _ in range(n + 1)]; ps[0] = 0; ps[1] = 0
for i in range(2, ceil(sqrt(n) + 1)):
    if ps[i] == 1:
        for j in range(2, n // i + 1):
            ps[j * i] = 0

