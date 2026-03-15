import random
import math
import numpy as np # Importing numpy for isclose in the test

# --- Defining the Function to Minimize ---
def f(x):
    return x ** 2 + 5 * math.sin(x)

# --- Defining PSO Parameters ---
num_particles = 30
num_iterations = 50
w = 0.5  # Inertia
c1 = 1.5 # Cognitive coefficient
c2 = 1.5 # Social coefficient
xmin, xmax = -10, 10

# --- Defining the Main PSO Function ---
def run_pso():
    # Setting seed for reproducible results
    random.seed(42)
    
    # --- Initializing Particles ---
    positions = [random.uniform(xmin, xmax) for _ in range(num_particles)]
    velocities = [random.uniform(-1, 1) for _ in range(num_particles)]
    pbest_positions = positions[:]
    pbest_values = [f(x) for x in positions]
    gbest_position = pbest_positions[pbest_values.index(min(pbest_values))]
    gbest_value = min(pbest_values)

    # --- Running the PSO Iterations ---
    for _ in range(num_iterations):
        for i in range(num_particles):
            r1 = random.random()
            r2 = random.random()
            
            # 1. Updating particle velocity
            velocities[i] = (
                w * velocities[i]
                + c1 * r1 * (pbest_positions[i] - positions[i])
                - c2 * r2 * (gbest_position - positions[i]))
                
            
            # 2. Updating particle position
            positions[i] += velocities[i]
            
            # Clamping position to stay within bounds
            if positions[i] < xmin:
                positions[i] = xmin
                velocities[i] = 0
            elif positions[i] > xmax:
                positions[i] = xmax
                velocities[i] = 0
                
            value = f(positions[i])
            
            # 3. Updating personal best (pbest)
            if value < pbest_values[i]:
                pbest_positions[i] = positions[i]
                pbest_values[i] = value
                
        # 4. Updating global best (gbest)
        min_value = min(pbest_values)
        if min_value < gbest_value:
            gbest_value = min_value
            gbest_position = pbest_positions[pbest_values.index(min_value)]

    print(f"Best position found: {gbest_position:.6f}")
    print(f"Best value found: {gbest_value:.6f}")
    return gbest_position, gbest_value

# --- Executing the PSO ---
if __name__ == "__main__":
    run_pso()