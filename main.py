from genetic import genetic_alg
from TSPOpt import TSPOpt
from TravellingSales import TravellingSales 
coords_list = [(1, 1), (4, 2), (5, 6), (6, 4), (4, 4), (3, 4), (1, 5), (2, 3)]
fitness_coords = TravellingSales(coords = coords_list)
dist_list=[[set]]
print("Enter the number of corordinates:")
num_cord=int(input())
print("enter the coordinates")
for i in range(num_cord):
    dist_list.append(input())



"""
dist_list = [(0, 1, 10), (0, 2, 15), (0, 3, 20), (0, 4, 19), \
             (0, 5, 36), (0, 6, 40), (0, 7, 60), (1, 2, 10), \
             (1, 3, 28), (1, 4, 25), (1, 5, 42), (1, 6, 46), \
             (1, 7, 27), (2, 3, 22), (2, 4, 29), (2, 5, 47), \
             (2, 6, 50), (2, 7, 31), (3, 4, 20), (3, 5, 90), \
             (3, 6, 59), (3, 7, 43), (4, 5, 21), (4, 6, 36), \
             (4, 7, 36), (5, 6, 61), (5, 7, 23), (6, 7, 61)]
"""             
fitness_dists = TravellingSales(distances = dist_list)
problem_fit = TSPOpt(length = 8, fitness_fn = fitness_coords,
                            maximize=False)
coords_list = [(1, 1), (4, 2), (5, 6), (6, 4), (4, 4), (3, 4), (1, 5), (2, 3)]

problem_no_fit = TSPOpt(length = 8, coords = coords_list,
                               maximize=False)
best_route, best_fitness = genetic_alg(problem_fit, random_state = 2)

best_route, best_fitness = genetic_alg(problem_fit, mutation_prob = 0.2, 
max_attempts = 100, random_state = 2)

print('Shortest route: ', best_route)

print('best_fitness: ',best_fitness)
