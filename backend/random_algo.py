'''
Description: This is an algorithm for comparison with the EA algorithm

Programmer: E Ching Kho
Disclaimer: This is for Queen's University CISC 455 Team Project
            Team member: E Ching Kho, Somoina Tian, Wenqi Tang
            Python Version 3.11.2 when developing
'''
# Import Files and Libraries
import numpy as np

def random_algo(total_tu=130, trend_mean=100, trend_sd=10, fluctuate_mean=0, fluctuate_sd=20):
    """
    Input: Integer - total_tu, Integer - trend_mean, Integer - trend_sd, Integer - fluctuate_mean, Integer - fluctuate_sd
    Ouput: [Float]
    Return a np.array of float values that represent the simulated stock price
    """
    return np.random.normal(trend_mean, trend_sd, total_tu) + np.random.normal(fluctuate_mean, fluctuate_sd, total_tu)