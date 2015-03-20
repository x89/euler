# Project Euler 76. How many ways can you write a sum of 100.

# Might we try some fancy memoization + iteration?
S = [0, 0, 1, 2, 4, 6, 10, 14, 22]

for N in range(9, 12):
    sumN = S[N-1]  # Start with set of S(n - 1)


            51
            42
    41      411
            33
    32      321
    311     3111
            222
    221     2211
    2111    21111
    11111   111111

# o(i,j) combinations beginning with i in N=j
# o(1,N) = 1
# o(N-1,N) = 1
# o(N-2,N) = 2 for N > 3
# o(N-3,N) = 3 for N > 4
#  o(2,5) = 3
#  o(3,6) = 3
#  o(6,9) = 3
# o(N-4,N) = ?
#  o(2,6) = 3
#  o(3,7) = 4
#  o(4,8) = 5
#  o(5,9) = 5

# o(2,3) = 1
# o(2,4) = 2
# o(2,5) = 2
# o(2,6) = 3
# o(2,20) = 10
# o(4,20) = 

# o(1,100) = 1
# o(2,100) = 50
# o(3,100) = 
# o(97,100) = 3
# o(98,100) = 2
# o(99,100) = 1
