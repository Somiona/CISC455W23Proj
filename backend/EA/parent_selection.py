"""
Description: A colleciton of parent selection methods

Programmer: 
Disclaimer: This is for Queen's University CISC 455 Team Project
            Team member: E Ching Kho, Somoina Tian, Wenqi Tang
            Python Version 3.11.2 when developing
"""
# Import Files and Libraries
import numpy as np


def ranking(population, fitness, rank_level = 5):
    """
    Input: [Investor] - population, [Float] - fitness, Integer - rank_level
    Output: [[Investor]]
    Separate the population into different rank level based on the fitness value
    """
    # Sort the population based on fitness in descending order
    sorted_population = [pop for _, pop in sorted(zip(fitness, population), reverse=True, key=lambda x: x[0])]
    # Calculate the size of each rank level
    rank_size = int(len(sorted_population) / rank_level)
    # Initialize the result list
    result = []
    # Iterate over the rank levels and append the corresponding sub-lists to the result list
    for i in range(rank_level):
        if i < rank_level - 1:
            result.append(sorted_population[i * rank_size:(i + 1) * rank_size])
        else:
            result.append(sorted_population[i * rank_size:])
    return result


def rank_pointer_selection(population, fitness, rank_level, mating_pool_size):
    """
    Input: [[Investor]] - rank_population, Integer - mating_pool_size >= 2
    Output: [Investor], len of mating_pool_size
    Description: rank_pointer_selection based on ranking function from above
    """
    mating_pool = []
    rank_population = ranking(population, fitness, rank_level)
    num_ranks = len(rank_population)
    count = 0

    # Ensure each rank is selected at least once, when mating_pool_size <= len(rank_population)
    for rank in rank_population:
        if count < mating_pool:
            chosen_individual = np.random.choice(rank)
            mating_pool.append(chosen_individual)
            count+=1
        else:
            return mating_pool

    # Perform remaining selections with equal probabilities
    remaining_selections = mating_pool_size - num_ranks
    for _ in range(remaining_selections):
        chosen_rank = np.random.choice(np.arange(num_ranks))
        chosen_individual = np.random.choice(rank_population[chosen_rank])
        mating_pool.append(chosen_individual)

    return mating_pool