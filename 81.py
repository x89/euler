# Project Euler 81. Shortest weighted path through a directed graph.

from pprint import pprint

lines = open('matrix.80x80.txt', 'r').readlines()
size = len(lines)  # NxN array
adj_values = []
for line in lines:
    line = line.split('\n')[0]
    adj_values.append(line.split(','))

adj_matrix = [[1000000 for _ in range(size**2)] for _ in range(size**2)]

for i in range(size ** 2):
    if i % size != size - 1:
        adj_matrix[i][i+1] = \
        int(adj_values[i//size%size][i%size+1])
    if i < size ** 2 - (size + 1):
        if i // size < size - 1:
            adj_matrix[i][i+size] = \
            int(adj_values[i//size%size+1][i%size])

shortest = [100000 for _ in range(size**2)]  # Shortest path v0 -> vN
shortest[0] = int(adj_values[0][0])

for v in range(len(adj_matrix)):
    row = adj_matrix[v]
    i = 0
    for c in row:
        if shortest[i] > c + shortest[v]:
            shortest[i] = c + shortest[v]
        i += 1

#for i in range(size):
#    print(shortest[i*size:(i+1)*size])

print(adj_values, shortest)

#print([{str(_): shortest[_]} for _ in range(len(shortest))])
