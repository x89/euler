# Project Euler 82. Shortest weighted path through a directed graph.
# It's the same as 84 with the code for moving left removed.
# And an iteration (for h in range(size)) to iterate over the adj matrix
# numerous times.

lines = open('p083_matrix.txt', 'r').readlines()
size = len(lines)
adj_values = []
for line in lines:
    line = line.split('\n')[0]
    adj_values.append([int(_) for _ in line.split(',')])
inf = 500000
adj_matrix = [[inf for _ in range(size**2)] for _ in range(size**2)]

for i in range(size ** 2):
    if i % size != size - 1:
        adj_matrix[i][i+1] = adj_values[i//size%size][i%size+1]
    if i < size ** 2 - (size + 1):
        if i // size < size - 1:
            adj_matrix[i][i+size] = adj_values[i//size%size+1][i%size]
    if i > size:
        adj_matrix[i][i-size] = adj_values[i//size%size-1][i%size]

shortest = [inf for _ in range(size**2)]
super_shortest = inf

for h in range(size):
    shortest[h*size] = adj_values[h][0]
    for _ in range(2):
        for v in range(len(adj_matrix)):
            row = adj_matrix[v]
            for index in (v+1, v+size, v-1, v-size):
                if index < 0 or index >= size**2:
                    continue
                c = row[index]
                if c + shortest[v] < shortest[index]:
                    shortest[index] = c + shortest[v]
        # loop through rightmost rows logging the shortest
        for i in [size * _ - 1 for _ in range(1, size)]:
            if shortest[i] < super_shortest:
                super_shortest = shortest[i]

print(super_shortest)
