# Project Euler 81. Shortest weighted path through a directed graph.

from pprint import pprint

lines = open('matrix.5x5.txt', 'r').readlines()
size = len(lines)  # NxN array
adjacency_values = []
for line in lines:
    line = line.split('\n')[0]
    adjacency_values.append(line.split(','))

adjacency_matrix = [[0 for _ in range(size**2)] for _ in range(size**2)]

for i in range(size ** 2):
    if i % size != size - 1:
        adjacency_matrix[i][i+1] = adjacency_values[i//size%size][i%size+1]
    if i < size ** 2 - (size + 1):
        if i // size < size - 1:
            adjacency_matrix[i][i+size+1] = adjacency_values[i//size%size+1][i%size]

total = adjacency_values[0][0]

