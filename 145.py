# Project Euler 145
# Reversible numbers are when n + reverse(n) consists only of odd numbers.
# There are 120 under 1000, how many under 10^9?

from sys import argv

max = int(argv[1]) or 100000000

#unchecked = [_ for _ in range(10, max + 1) if str(_)[-1] != '0']

n = 0

for x in range(10, max + 1):
    if x % 10 == 0:  # Ignore suffixed-by-zero
        continue
    y = str(x)[::-1]
    z = x + int(y)
    zstr = str(z)
    if '2' not in zstr and '4' not in zstr \
            and '6' not in zstr and '8' not in zstr and '0' not in zstr:
        n += 1
        #print(n, x, y, z)

print(n)

# Only need to check up to 10^8 as there are no 7 + reverse(7) digit numbers
# that have no even numbers in them. (Nor are there 5 + reverse(5).)
# Too slow! 3m14s. Pure brute force.
# Not exactly sure what the relation between orders of magnitude is but I'm
# certain there is one. From 100: 20, 120, 720, 720, 18720, ...
