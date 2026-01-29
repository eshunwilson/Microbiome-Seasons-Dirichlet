# Simulation of sesonal changes of microbiome using Dirichlet sampling

import numpy as np
import matplotlib.pyplot as plt

# Parameters
seasons = ["Spring", "Summer", "Fall", "Winter"]
T = 10  # Number of time steps (years)
pool_mixing_rate = 0.2  # Microbial transfer rate
growth_rate = 0.1  # Growth rate
fitness_factor = [1.2, 1.5, 0.8, 1.0]  # Fitness variation across seasons

# Initialize microbial population (fraction of 3 microbial types)
population = np.random.dirichlet([2, 3, 4])  # Random initial proportions

# Function: Horizontal Mixing (Microbial Transfer)
def horizontal_mixing(pop, rate):
    """ Redistributes microbes across the environment """
    mean_pop = np.mean(pop)
    return (1 - rate) * pop + rate * mean_pop  # Weighted redistribution

# Function: Microbial Growth (Logistic Growth)
def microbial_growth(pop, growth_rate):
    """ Models microbial growth with a carrying capacity """
    K = 1  # Carrying capacity (population sum must stay 1)
    return pop + growth_rate * pop * (1 - np.sum(pop) / K)

# Function: Selection (Fitness-Based Adjustment)
def selection(pop, fitness):
    """ Adjusts microbial proportions based on seasonal fitness """
    return pop * fitness / np.sum(pop * fitness)  # Normalize to maintain proportions

# Simulation Loop
history = []

for t in range(T):
    season = seasons[t % 4]  # Cycle through seasons
    print(f"Year {t+1} - {season}")

    # Step 1: Microbial Mixing
    population = horizontal_mixing(population, pool_mixing_rate)

    # Step 2: Microbial Growth
    population = microbial_growth(population, growth_rate)

    # Step 3: Selection Based on Seasonal Fitness
    population = selection(population, fitness_factor[t % 4])

    # Store results
    history.append(population.copy())

    # Plot microbial composition over time
    plt.figure(figsize=(6, 4))
    plt.bar(["Microbe 1", "Microbe 2", "Microbe 3"], population, color=['skyblue', 'blue', 'darkblue'])
    plt.title(f"Microbial Composition - Year {t+1} ({season})")
    plt.ylabel("Proportion")
    plt.ylim(0, 1)
    plt.show()
