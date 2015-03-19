# Project Euler 83. Shortest weighted path through a directed graph.

#lines = open('matrix.5x5.txt', 'r').readlines()
lines = open('p083_matrix.txt', 'r').readlines()
size = len(lines)  # NxN array
adj_values = []
for line in lines:
    line = line.split('\n')[0]
    adj_values.append([int(_) for _ in line.split(',')])
inf = 500000  # Set to higher than anything in our matrix
adj_matrix = [[inf for _ in range(size**2)] for _ in range(size**2)]

for i in range(size ** 2):
    if i % size != size - 1:
        adj_matrix[i][i+1] = adj_values[i//size%size][i%size+1]
    if i < size ** 2 - (size + 1):
        if i // size < size - 1:
            adj_matrix[i][i+size] = adj_values[i//size%size+1][i%size]
    # Code for #83, going left / up!
    if i % size != 0:
        adj_matrix[i][i-1] = adj_values[i//size%size][i%size-1]
    if i > size:
        adj_matrix[i][i-size] = adj_values[i//size%size-1][i%size]

i = 0
while i < size ** 2:
    # Check that the adj matrix has a matching entry where it should.
    if i + size < size ** 2 - 1:
        assert adj_matrix[i][i+size] < inf, "%d, %d" % (i, i+size)
    if not (i + 1) % size == 0:
        assert adj_matrix[i][i+1] < inf, "%d, %d" % (i, i+1)
    if i > size:
        assert adj_matrix[i][i-size] < inf, "%d, %d" % (i, i-size)
    if i % size != 0:
        assert adj_matrix[i][i-1] < inf, "%d, %d" % (i, i-1)
    i += 1

shortest = [inf for _ in range(size**2)]  # Shortest path v0 -> vN
shortest[0] = int(adj_values[0][0])

for _ in range(4):  # Filthy hack. We have to reverse 5 times.
    for v in range(len(adj_matrix)):
        row = adj_matrix[v]
        for index in (v+1, v+size, v-1, v-size):
            if index < 0 or index >= size**2:
                continue
            c = row[index]
            if c + shortest[v] < shortest[index]:
                shortest[index] = c + shortest[v]

#for i in range(size):
#    print(shortest[i*size:((i*size)+size)])

print(shortest[-1])
