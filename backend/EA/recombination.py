"""
Description: A colleciton of recombination methods
Programmer:
Disclaimer: This is for Queen's University CISC 455 Team Project
            Team member: E Ching Kho, Somoina Tian, Wenqi Tang
            Python Version 3.11.2 when developing
"""

import numpy as np


### This is used for testing purpose
class Individual:
    def __init__(self, wallet, emotional_resiliency, ann, age, death_age):
        self.wallet = wallet
        self.emotional_resiliency = emotional_resiliency
        self.ann = ann
        self.age = age
        self.death_age = death_age


class ANN:
    def __init__(self, weights):
        self.weights = weights

### The code below are the real one

def teach_me_something_bro(population, individual1, individual2, alpha, beta):
    # Determine which individual is less fit
    if individual1.wallet < individual2.wallet:
        learner, fitter = individual1, individual2
    else:
        learner, fitter = individual2, individual1

    # Calculate learning distance for ANN
    learn_distance = np.array(fitter.ann.weights) - np.array(learner.ann.weights)

    # Update learner's ANN
    learner.ann.weights += alpha * learn_distance

    # Update fitter's ANN
    fitter.ann.weights += (1 - alpha) / 2 * (-learn_distance)

    # Calculate thank you money
    thank_you_money = learner.wallet * beta

    # Update wallets
    learner.wallet -= thank_you_money
    fitter.wallet += thank_you_money


def new_investors(population, new_investors_list):
    # Identify individuals that have reached their death age
    dead_individuals = [ind for ind in population if ind.age >= ind.death_age]

    # Replace dead individuals with new investors
    for dead_ind, new_investor in zip(dead_individuals, new_investors_list):
        population[population.index(dead_ind)] = new_investor


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


### Now it is time to test those functions

if __name__ == "__main__":
    # Example population
    population = [
        Individual(100, 0.5, ANN([1, 2, 3]), 3, 10),
        Individual(200, 0.6, ANN([4, 5, 6]), 5, 15),
        Individual(300, 0.7, ANN([7, 8, 9]), 8, 20),
    ]

    # Print the initial population
    print("Initial population:")
    for ind in population:
        print(vars(ind))

    # Example recombinations
    recombinations = [
        {
            'type': 'absolute',
            'function': teach_me_something_bro,
            'args': (population[0], population[1], 0.5, 0.25),
        },
        {
            'type': 'periodic',
            'function': new_investors,
            'period': 5,
            'args': ([Individual(400, 0.8, ANN([10, 11, 12]), 0, 10)],),
        },
    ]

    generation = 5
    recombination_transformation(population, generation, recombinations)

    # Print the population after applying the recombinations
    print("\nPopulation after recombination transformation:")
    for ind in population:
        print(vars(ind))
