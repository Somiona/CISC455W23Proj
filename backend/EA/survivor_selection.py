"""
Description: A colleciton of survivor selection methods
Programmer:
Disclaimer: This is for Queen's University CISC 455 Team Project
            Team member: E Ching Kho, Somoina Tian, Wenqi Tang
            Python Version 3.11.2 when developing
"""

import random

class ANN:
    def __init__(self, weights):
        self.weights = weights

class Individual:
    def __init__(self, wallet, threshold, ann, age, death_age):
        self.wallet = wallet
        self.threshold = threshold
        self.ann = ann
        self.age = age
        self.death_age = death_age

def hybrid_environment_selection(population, dead_individuals, heritage_option, lambda_individuals):
    # Create new individuals based on (μ+λ)
    new_individuals = [Individual(random.randint(100, 500), random.uniform(0.5, 0.9),
                                  ANN([random.randint(1, 10) for _ in range(3)]),
                                  0, random.randint(10, 25))
                       for _ in range(lambda_individuals)]

    # Add new individuals to the population
    population.extend(new_individuals)

    # Handle dead individuals' assets
    if heritage_option == "heritage":
        for dead_ind in dead_individuals:
            group = random.sample(population, len(population) // 2)
            total_assets = dead_ind.wallet / len(group)
            for ind in group:
                ind.wallet += total_assets
    elif heritage_option == "straight_delete":
        pass
    elif heritage_option == "uniform_distribution":
        for dead_ind in dead_individuals:
            total_assets = dead_ind.wallet / len(population)
            for ind in population:
                ind.wallet += total_assets
    elif heritage_option == "lucky_guy":
        for dead_ind in dead_individuals:
            lucky_ind = random.choice(population)
            lucky_ind.wallet += dead_ind.wallet

    # Remove dead individuals from the population
    for dead_ind in dead_individuals:
        population.remove(dead_ind)

def evolution(population, max_generations, termination_halt, lambda_individuals, heritage_option):
    generation = 0
    halted_generations = [0] * len(population)
    last_wallets = [ind.wallet for ind in population]

    while generation < max_generations:
        # Increase the age of every individual
        for ind in population:
            ind.age += 1

        # Handle dead individuals
        dead_individuals = [ind for ind in population if ind.age >= ind.death_age]
        hybrid_environment_selection(population, dead_individuals, heritage_option, lambda_individuals)

        # Update last_wallets and halted_generations to include new individuals
        last_wallets = [ind.wallet for ind in population]
        halted_generations = [0] * len(population)

        # Termination condition - halt (hold for more than 3 generations)
        halt_count = 0
        for i, ind in enumerate(population):
            if abs(ind.wallet - last_wallets[i]) < 1e-6:
                halted_generations[i] += 1
            else:
                halted_generations[i] = 0

            if halted_generations[i] >= termination_halt:
                halt_count += 1

            last_wallets[i] = ind.wallet

        if halt_count == len(population):
            print(f"Termination condition reached at generation {generation}. All individuals halted.")
            break

        generation += 1

    return population




if __name__ == "__main__":
    # Example population
    population = [
        Individual(100, 0.5, ANN([1, 2, 3]), 3, 10),
        Individual(200, 0.6, ANN([4, 5, 6]), 5, 15),
        Individual(300, 0.7, ANN([7, 8, 9]), 8, 20),
]
max_generations = 100
termination_halt = 3
lambda_individuals = 2
heritage_option = "heritage"

final_population = evolution(population, max_generations, termination_halt, lambda_individuals, heritage_option)

# Print the final population
print("\nFinal population:")
for ind in final_population:
    print(vars(ind))
