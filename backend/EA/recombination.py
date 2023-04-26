"""
Description: A collection of recombination methods

Programmer: Wenqi Tang, E Ching Kho
Disclaimer: This is for Queen's University CISC 455 Team Project
            Team member: E Ching Kho, Somoina Tian, Wenqi Tang
            Python Version 3.11.2 when developing
"""
# Import Files and Libraries
import numpy as np
from evaluation import asset_fitness


# Recombination functions
def teach_me_something_bro(individual1, individual2, alpha, beta):
    # Determine which individual is fitter
    if asset_fitness(individual1) < asset_fitness(individual2):
        learner, fitter = individual1, individual2
    else:
        learner, fitter = individual2, individual1

    # Calculate learning distance for ANN
    layer_names = fitter.ann.layer_name
    learn_distance = {weights:fitter.ann.get_weights(False)[weights] - learner.ann.get_weights(False)[weights] for weights in layer_names}

    # Update learner's ANN
    learner.ann.add_everything({weights:learn_distance[weights] * alpha for weights in layer_names})

    # Update fitter's ANN
    fitter.ann.add_everything({weights:learn_distance[weights] * -(1-alpha)/2 for weights in layer_names})

    # Calculate thank you money
    thank_you_money = np.round(learner.wallet * beta,2)

    # Update wallets
    learner.add_wallet(-thank_you_money)
    fitter.add_wallet(thank_you_money)


def new_investors(parents, new_ind_size, mutation):
    """
    Input: [Investor] - parents, Integer - new_ind_size
    Output: [Investor]
    """
    pass



# Add other recombination functions here

def recombination_transformation(population, generation, recombinations):
    """
    Performs a recombination transformation on a population, given its current generation and a list of
    recombination dictionaries.

    Args:
        population (list): The population on which the recombinations will be applied.
        generation (int): The current generation number of the evolutionary process.
        recombinations (list): List of recombination dictionaries containing recombination types, conditions, and functions.
    """

    # Iterate through the list of recombination dictionaries
    for recombination in recombinations:
        # Absolute Recombination
        if recombination['type'] == 'absolute':
            # Apply the recombination function specified in the recombination dictionary with the additional arguments
            recombination['function'](population, *recombination['args'])

        # Periodic Recombination
        elif recombination['type'] == 'periodic':
            # Check if the current generation is a multiple of the period specified in the recombination dictionary
            if generation % recombination['period'] == 0:
                # Apply the recombination function specified in the recombination dictionary with the additional arguments
                recombination['function'](population, *recombination['args'])

        # Probabilistic Recombination
        elif recombination['type'] == 'probabilistic':
            # Check if a random uniform number is less than the probability specified in the recombination dictionary
            if np.random.uniform() < recombination['probability']:
                # Apply the recombination function specified in the recombination dictionary with the additional arguments
                recombination['function'](population, *recombination['args'])

# # Test the functions
# if __name__ == "__main__":
#     # Example population
#     population = [
#         Individual(100, 0.5, ANN([1, 2, 3]), 3, 10),
#         Individual(200, 0.6, ANN([4, 5, 6]), 5, 15),
#         Individual(300, 0.7, ANN([7, 8, 9]), 8, 20),
#     ]

#     # Print the initial population
#     print("Initial population:")
#     for ind in population:
#         print(vars(ind))

#     # Example recombinations
#     recombinations = [
#         {
#             'type': 'absolute',
#             'function': teach_me_something_bro,
#             'args': (population[0], population[1], 0.5, 0.25),
#         },
#         {
#             'type': 'periodic',
#             'function': new_investors,
#             'period': 5,
#             'args': ([Individual(400, 0.8, ANN([10, 11, 12]), 0, 10)],),
#         },
#     ]

#     generation = 5
#     recombination_transformation(population, generation, recombinations)

#     # Print the population after applying the recombinations
#     print("\nPopulation after recombination transformation:")
#     for ind in population:
#         print(vars(ind))

