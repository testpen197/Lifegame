import numpy as np
import time

# Créer la grille initiale 7x7
grille = np.zeros((7, 7), dtype=int)
grille[3, 2:5] = 1  # ligne de 3 cellules vivantes au milieu

def add_padding(g):
    return np.pad(g, 1, mode='constant')

def count_neighbors(padded, row, col):
    total = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            total += padded[row + i, col + j]
    return total

def next_generation(g):
    padded = add_padding(g)
    new_g = np.zeros_like(g)
    
    for i in range(g.shape[0]):
        for j in range(g.shape[1]):
            neighbors = count_neighbors(padded, i + 1, j + 1)
            cell = g[i, j]
            
            if cell == 1:
                if neighbors == 2 or neighbors == 3:
                    new_g[i, j] = 1
                else:
                    new_g[i, j] = 0
            else:
                if neighbors == 3:
                    new_g[i, j] = 1
                else:
                    new_g[i, j] = 0
    
    return new_g

def display(g):
    for row in g:
        print(' '.join(['█' if x else '·' for x in row]))
    print()

# Simulation
current = grille.copy()
gen = 0

while gen < 8:
    print(f"Gen {gen}")
    display(current)
    current = next_generation(current)
    time.sleep(0.5)
    gen += 1