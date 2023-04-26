"""
Description: A collection of evaluation methods

Programmer: E Ching Kho
Disclaimer: This is for Queen's University CISC 455 Team Project
            Team member: E Ching Kho, Somoina Tian, Wenqi Tang
            Python Version 3.11.2 when developing
"""
# Import Files and Libraries
import numpy as np


def asset_fitness(individual, alpha=0.5):
    """
    Input: Investor - individual, [Stock] - market, np.float32 - alpha
    Output: int, an integer value representation its individual's fitness
    """
    return alpha * np.float32(individual.wallet) + (1-alpha) * np.sum([share.price for shares in individual.shares.values() for share in shares])


def zero_sum_fitness(individual, individuals):
    pass

def potential_growth_fitness(individual):
    pass


