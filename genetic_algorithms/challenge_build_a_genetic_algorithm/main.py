import random
import numpy as np

# --- Defining Constants ---
POP_SIZE = 20
X_MIN, X_MAX = 0, 6

# --- Defining Helper Functions ---

# Defining the function to maximize
def fitness_function(x):
    return -(x - 3) ** 2 + 10

# Initializing the population
def init_population():
    return [random.uniform(X_MIN, X_MAX) for _ in range(POP_SIZE)]

# Defining tournament selection
def tournament_selection(pop, fit, k=3):
    selected = random.sample(list(zip(pop, fit)), k)
    selected.sort(key=lambda t: t[1], reverse=True)
    return selected[0][0]

# Defining arithmetic crossover
def arithmetic_crossover(parent1, parent2):
    alpha = random.uniform(0, 1)
    return alpha * parent1 + (1 - alpha) * parent2

# Defining mutation
def mutate(x):
    x_new = x + np.random.normal(0, 0.1)
    return min(max(x_new, X_MIN), X_MAX)

# --- Defining the Main GA Function ---
def genetic_algorithm():
    # Setting seeds for reproducible results
    random.seed(42)
    np.random.seed(42)
    
    population = init_population()
    best_fitness = None
    best_x = None
    no_improve = 0
    max_generations = 200

    # --- Main Evolution Loop ---
    for generation in range(max_generations):
        # 1. Evaluating the population
        fitness = [fitness_function(x) for x in population]
        
        # 2. Finding the best individual in this generation
        gen_best_idx = np.argmax(fitness)
        gen_best_fit = fitness[gen_best_idx]
        gen_best_x = population[gen_best_idx]
        
        # Tracking the best-ever solution
        if best_fitness is None or gen_best_fit > best_fitness:
            best_fitness = gen_best_fit
            best_x = gen_best_x
            no_improve = 0
        else:
            no_improve += 1
            
        # Stopping if no improvement
        if no_improve >= 20:
            break
            
        new_population = []
        while len(new_population) < POP_SIZE:
            # 3. Creating a new individual
            # Selecting parents
            parent1 = tournament_selection(population, fitness)
            parent2 = tournament_selection(population, fitness)
            # Performing crossover
            child = arithmetic_crossover(parent1, parent2)
            # Performing mutation
            child = mutate(child)
            
            new_population.append(child)
            
        # 4. Replacing the old population
        population = new_population
        
    print(f"Best solution: x = {best_x:.4f}, fitness = {best_fitness:.4f}")
    return best_x, best_fitness

# --- Running the Algorithm ---
if __name__ == "__main__":
    genetic_algorithm()