# using this as example: https://www.educative.io/answers/solving-the-8-queen-problem-using-genetic-algorithm

# Need to initialize a board state, in this case its randomly generated
# Fitness evaluation, how many non-attacking pairs are there?
# Fitness is calculated by adding the # of non-attacking pairs of each queen
# Selection of best genomes
# Crossover to make offspring
# In this case, we'll cross over every value beyond the 3rd Index between the two parents

# Repeat

# In this example, Rows and columns are switched. Index = Columns and rows = values

import random

# Params
POPULATION_SIZE = 100
MUTATION_RATE = 0.1
MAX_GENERATIONS = 1000
numQueens = 8
max_fitness = 28


# Generate Random Board State (Initialization)
def generate_board_state():
    board_state = [random.randint(0, 7) for _ in range(numQueens)]
    return board_state

# Calc Fitness scores
def calculate_fitness(board_state):
    conflicts = 0
    for i in range(numQueens):
        for j in range(i + 1, numQueens):
            if board_state[i] == board_state[j] or abs(board_state[i] - board_state[j]) == j - i:
                conflicts += 1
    return max_fitness - conflicts

def tournament_selection(population):
    tournament_size = 5
    tournament = random.sample(population, tournament_size)
    return max(tournament, key=lambda x: x[1])

# key uses a function to grab the index 1 element on list x, then finds the max of those but keeps the list

def crossover(parent1, parent2): 
    crossover_point = random.randint(1,7)
    # finds random place to splice genome
    # returns child with combined characteristics, divided at crossover point
    child = parent1[:crossover_point] + parent2[crossover_point:]
    return child

def mutate(board_state):
    pos1, pos2 = random.sample(range(8), 2)
    board_state[pos1], board_state[pos2] = board_state[pos2], board_state[pos1]
    return board_state

population = [(generate_board_state(), 0) for _ in range(POPULATION_SIZE)]

# Gen Algo loop

for generation in range(MAX_GENERATIONS):
    population = [(board_state, calculate_fitness(board_state)) for board_state, _ in population]

    best_board_state = max(population, key=lambda x: x[1])[0]

    if calculate_fitness(best_board_state) == 28:
        print("Solution found in generation: ", generation)
        break

    # Generate next gen
    new_population = []

    new_population.append(max(population, key=lambda x: x[1]))

    while len(new_population) < POPULATION_SIZE:
        parent1 = tournament_selection(population)
        parent2 = tournament_selection(population)
        child = crossover(parent1[0], parent2[0])
        if random.random() < MUTATION_RATE:
            child = mutate(child)
        new_population.append((child, 0))
    
    population = new_population


print("Best Soln: ", best_board_state)

# Looks like it won't find the perfect solution every time but gets close depending on parameters
