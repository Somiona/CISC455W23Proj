"""
Description: A colleciton of mutation methods
Programmer:
Disclaimer: This is for Queen's University CISC 455 Team Project
            Team member: E Ching Kho, Somoina Tian, Wenqi Tang
            Python Version 3.11.2 when developing
"""

import numpy as np
import random


### This is used for testing purpose
class SimpleANN:
    def __init__(self, weights):
        self.weights = weights


class Individual:
    def __init__(self, wallet, emotional_resiliency, ann, shares_hold):
        self.wallet = wallet
        self.emotional_resiliency = emotional_resiliency
        self.ann = ann
        self.shares_hold = shares_hold


### The code below are the real one


# Decreases emotional resiliency (bounded between [0, 1])
def emotional_damage(individual):
    # Subtract a random value between 0 and 1 from emotional resiliency, and clip it to be within the range [0, 1]
    individual.emotional_resiliency = max(0, individual.emotional_resiliency - np.random.uniform())


# Increases emotional resiliency (bounded between [0, 1])
def emotion_okay_lah(individual):
    # Add a random value between 0 and 1 to emotional resiliency, and clip it to be within the range [0, 1]
    individual.emotional_resiliency = min(1, individual.emotional_resiliency + np.random.uniform())


# Increases wallet amount and lowers emotional resiliency
def get_salary(individual, gain_wallet):
    individual.wallet += gain_wallet
    # Update emotional resiliency by multiplying it with (1 - gain_wallet)
    individual.emotional_resiliency *= (1 - gain_wallet)


# Decreases wallet amount and raises emotional resiliency
def pay_for_survival(individual, loss_wallet):
    individual.wallet -= loss_wallet
    # Update emotional resiliency by multiplying it with (1 + loss_wallet)
    individual.emotional_resiliency *= (1 + loss_wallet)


# Modifies a random neuron's weight in the ANN model based on the best individual
def continuous_learning(individual, best_individual):
    # Select a random weight index
    random_weight_index = random.randint(0, len(individual.ann.weights) - 1)
    # Clone the weight from the best individual
    individual.ann.weights[random_weight_index] = best_individual.ann.weights[random_weight_index]


# Adds a random value (from a normal distribution) to some weights of an individual's ANN model
def maybe_i_should_change(individual, sigma):
    num_weights = len(individual.ann.weights)
    # Select a random number of weights to change
    num_weights_to_change = random.randint(1, num_weights)
    for _ in range(num_weights_to_change):
        # Select a random weight index
        random_weight_index = random.randint(0, num_weights - 1)
        # Add a random value from a normal distribution with mean 0 and standard deviation sigma
        individual.ann.weights[random_weight_index] += np.random.normal(0, sigma)


# Modifies wallet, emotional resiliency, ANN, or shares_hold with equal probability
def life_is_uncertain(individual, config):
    # Select a random event
    event = random.choice(['wallet', 'emotion_resiliency', 'ann', 'shares_hold'])

    if event == 'wallet':
        # Update wallet with a random value from a normal distribution with mean 0 and standard deviation specified in config
        individual.wallet += np.random.normal(0, config['life_is_uncertain_sigma_wallet'])

    elif event == 'emotion_resiliency':
        # Update emotional resiliency with a random value from a normal distribution with mean 0 and standard deviation specified in config
        new_resiliency = individual.emotional_resiliency + np.random.normal(0, config[
            'life_is_uncertain_sigma_emotion_resiliency'])
        # Clip the new value to be within the range [0, 1]
        individual.emotional_resiliency = np.clip(new_resiliency, 0, 1)

    elif event == 'ann':
        # Select a random weight index
        random_weight_index = random.randint(0, len(individual.ann.weights) - 1)
        # Add a random value from a normal distribution with mean 0 and standard deviation specified in config
        individual.ann.weights[random_weight_index] += np.random.normal(0, config['life_is_uncertain_sigma_ann'])

    elif event == 'shares_hold':
        if len(individual.shares_hold) > 0:
            # Randomly select a stock
            random_stock = random.choice(individual.shares_hold)
            # Randomize its fail to sell counter between [0, 10]
            random_stock.fail_to_sell_counter = random.randint(0, 10)
        else:
            # Do nothing if the individual has no shares
            pass


def mutation_transformation(individual, best_individual, config, generation, mutations):
    """
    Performs a mutation transformation on an individual, given its current generation, the
    user-configured mutation settings, and a list of mutation dictionaries.

    Args:
        individual (object): The individual on which the mutations will be applied.
        best_individual (object): The current best individual in the population, used for continuous learning.
        config (dict): The configuration dictionary containing user-configured mutation settings.
        generation (int): The current generation number of the evolutionary process.
        mutations (list): List of mutation dictionaries containing mutation types, conditions, and functions.
    """

    # Iterate through the list of mutation dictionaries
    for mutation in mutations:
        # Conditional Mutation
        if mutation['type'] == 'conditional':
            # Check if the condition specified in the mutation dictionary is satisfied
            if mutation['condition'](individual):
                # Apply the mutation function specified in the mutation dictionary
                mutation['function'](individual)

        # Periodic Mutation
        elif mutation['type'] == 'periodic':
            # Check if the current generation is a multiple of the period specified in the mutation dictionary
            if generation % mutation['period'] == 0:
                # Apply the mutation function specified in the mutation dictionary with the additional arguments
                mutation['function'](individual, *mutation['args'])

        # Probabilistic Mutation
        elif mutation['type'] == 'probabilistic':
            # Check if a random uniform number is less than the probability specified in the mutation dictionary
            if np.random.uniform() < mutation['probability']:
                # Apply the mutation function specified in the mutation dictionary with the additional arguments
                mutation['function'](individual, *mutation['args'])


### Now it is time to test those functions

if __name__ == "__main__":
    # Create a simple configuration dictionary for testing purposes
    config = {
        'life_is_uncertain_sigma_wallet': 100,
        'life_is_uncertain_sigma_emotion_resiliency': 1/3,
        'life_is_uncertain_sigma_ann': 0.1,
    }

    # Create a simple ANN model for testing purposes
    ann1 = SimpleANN([0.1, 0.2, 0.3])
    ann2 = SimpleANN([0.4, 0.5, 0.6])

    # Create two individuals for testing purposes
    individual1 = Individual(1000, 0.5, ann1, [])
    individual2 = Individual(2000, 0.7, ann2, [])

    # Set the best individual
    best_individual = individual2

    # Set the current generation
    generation = 1

    # Create a list of mutation dictionaries for testing purposes
    mutations = [
        {
            'type': 'conditional',
            'condition': lambda ind: ind.wallet > 1500,
            'function': emotional_damage,
        },
        {
            'type': 'periodic',
            'period': 3,
            'function': get_salary,
            'args': [500],
        },
        {
            'type': 'probabilistic',
            'probability': 0.5,
            'function': maybe_i_should_change,
            'args': [0.1],
        },
        {
            'type': 'probabilistic',
            'probability': 0.3,
            'function': life_is_uncertain,
            'args': [config],
        },
    ]

    # Apply mutation transformation to the individual
    mutation_transformation(individual1, best_individual, config, generation, mutations)

    # Print the individual's properties after mutation
    print("Wallet:", individual1.wallet)
    print("Emotional resiliency:", individual1.emotional_resiliency)
    print("ANN weights:", individual1.ann.weights)