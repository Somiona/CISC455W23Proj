"""
Description: A colleciton of mutation methods
Programmer: Wenqi Tang, E Ching Kho
Disclaimer: This is for Queen's University CISC 455 Team Project
            Team member: E Ching Kho, Somoina Tian, Wenqi Tang
            Python Version 3.11.2 when developing
"""
# Import Files and Libraries
import numpy as np


class Mutation:
    curr_gen = 0 # When initialization, the current generation is 0
    
    def __init__(self, individual, type, probability, functions, num_gen=0, start_gen=0, cycle_num=1, conditions=None, arguments=None):
        """
        Input: Investor - individual, String - type, Float - probability, [function] - functions, Integer - num_gen, Integer - start_gen, Integer - cycle_num, [lambda function] - conditions, [Float] - arguments
        Output: None
        Description: Initialize Mutation
        """
        self.individual = individual
        self.type = type
        self.probability = probability
        self.functions = functions
        self.cycle = np.arange(start_gen, num_gen, cycle_num)
        self.conditions = conditions
        self.arguments = arguments
        self.start_gen = start_gen
    
    def decide_function(self):
        if np.random.rand() <= self.probability: # Determine if this mutation occurs
            if self.conditions == None:
                # type is either "periodic" or "probablistic"
                if len(self.cycle) == 0:
                    # type is "probablistic"
                    self.run_check_has_arguments(0)
                else:
                    # type is "periodic"
                    if self.curr_gen in self.cycle:
                        self.run_check_has_arguments(0)
            else:
                # type is "conditional"
                for i in range(len(self.conditions)):
                    if self.conditions[i](self.individual):
                        self.run_check_has_arguments(i)    

    def run_check_has_arguments(self, i):
        if self.arguments != None:
            self.functions[i](self.individual, *self.arguments)
        else:
            self.functions[i](self.individual)
    
    
def emotional_damage(individual):
    """
    Input: Investor - individual
    Output: None
    Description: Decreases the individual's emotional resiliency by a random value between 0 and 1 (bounded between [0, 1])
    """
    # Subtract a random value between 0 and 1 from emotional resiliency, and clip it to be within the range [0, 1]
    # individual.emotion = max(0, individual.emotion - np.random.uniform()/5)
    individual.emotion = max(0, individual.emotion - 0.1)


def emotion_okay_lah(individual):
    """
    Input: Investor - individual
    Output: None
    Description: Increase the individual's emotional resiliency by a random value between 0 and 1 (bounded between [0, 1])
    """
    # Add a random value between 0 and 1 to emotional resiliency, and clip it to be within the range [0, 1]
    individual.emotion = min(1, individual.emotion + np.random.uniform()/5) 
    individual.emotion = min(1, individual.emotion + 0.1) 


def get_salary(individual, gain_wallet):
    """
    Input: Investor - individual, Float - gain_wallet
    Output: None
    Description: Increases wallet amount and lowers emotional resiliency
    """
    individual.wallet += gain_wallet
    # Update emotional resiliency by multiplying it with (1 - gain_wallet/individual.wallet)
    individual.emotion *= (1 - gain_wallet/individual.wallet)


def pay_for_survival(individual, loss_wallet):
    """
    Input: Investor - individual, Float - loss_wallet
    Output: None
    Description: Decrease wallet amount and raises emotional resiliency
    """
    individual.wallet -= loss_wallet
    # Update emotional resiliency by multiplying it with (1 + loss_wallet/individual.wallet)
    individual.emotion *= (1 + loss_wallet/individual.wallet)


def learn_from_rich(individual, best_individual):
    """
    Input: Investor - individual, Investor - best_individual
    Output: None
    Description: Modifies a random neuron's weight in the individual's ANN model based on the best individual
    """
    # Select a random weight index
    random_weight_index = np.random.choice(np.arange(individual.ann.total_weights))
    # Clone the weight from the best individual
    individual.ann.update_weight(random_weight_index, best_individual.ann.get_weight(random_weight_index))


def maybe_i_should_change(individual, sigma):
    """
    Input: Investor - individual, Float - sigma
    Output: None
    Description: Add random values (from a normal distribution) to some weights of an individual's ANN model
    """
    # Select a random number of weights to change
    num_weights_to_change = np.random.choice(np.arange(1,individual.ann.total_weights))

    # Randomly choice those weights
    random_weight_indices = np.random.choice(np.arange(individual.ann.total_weights, dtype=int), num_weights_to_change, replace=False)

    # Add random values from a normal distribution with mean 0 and standard deviation sigma to those weights
    individual.ann.add_weights(random_weight_indices, np.random.normal(0, sigma, num_weights_to_change))
    

def life_is_uncertain(individual, config={"wallet": 50,"emotion": 0.1,"ann": 0.01}, probabilities=np.ones(4)/4):
    """
    Input: Investor - individual, {String: Float} - config, [Float] - probabilities,
    Output: None
    Description: randomly modifies individual's wallet, emotional resiliency, ANN, or shares_hold based on given probabilities
                 config = {
                    "wallet": 50,
                    "emotion": 0.1,
                    "ann": 0.03
                 } which is preset modification
    """
    # Select a random event
    event = np.random.choice(['wallet', 'emotion_resiliency', 'ann', 'shares_hold'])
    
    if event == 'wallet':
        # Update wallet with a random value from a normal distribution with mean 0 and standard deviation specified in config
        individual.add_wallet(np.random.normal(0, config["wallet"]))

    elif event == 'emotion_resiliency':
        # Update emotional resiliency with a random value from a normal distribution with mean 0 and standard deviation specified in config
        individual.add_emotion(np.random.normal(0, config["emotion"]))

    elif event == 'ann':
        maybe_i_should_change(individual, config["ann"])

    elif event == 'shares_hold':
        # Randomly select a stock
        stock_shares = individual.shares[np.random.choice([stock for stock in individual.shares.keys()])]
        if stock_shares:
            # Randomly select a share
            share = np.random.choice(stock_shares)
            # Randomize its failed selling counter between [0, 10]
            share.failed_selling = np.random.choice(np.arange(11))


def mutation_transformation(individual, prob_list, best_ind, num_gen, start_gen, cycles, emo_cond, sal_peri, pay_peri, learn_peri, change, uncertain):
    """
    Input: Investor - individual, [Float] - prob_list, Investor - best_ind, Integer - num_gen, [Integer] - start_gen, [Integer] - cycles, Boolean - emo_cond, Boolean - sal_peri, Boolean - pay_peri, Boolean - learn_peri, Boolean - change, Boolean - uncertain
    Output: [Mutation]
    Description: initialize a list of Mutation
    """
    mu_list = []
    if emo_cond:
        mu_list.append(Mutation(individual, "Conditional", 1, [emotional_damage, emotion_okay_lah],conditions=[lambda ind: ind.action_value == 0, lambda ind: ind.action_value != 0]))
    if sal_peri:
        mu_list.append(Mutation(individual, "periodic", 1, [get_salary], num_gen, start_gen[0], cycles[0], arguments=[np.random.normal(100, 15)]))
    if pay_peri:
        mu_list.append(Mutation(individual, "periodic", 1, [pay_for_survival], num_gen, start_gen[1], cycles[1], arguments=[np.random.normal(50, 10)]))
    if learn_peri:
        mu_list.append(Mutation(individual, "periodic", 1, [learn_peri], num_gen, start_gen[2], cycles[2], arguments=[best_ind]))
    if change:
        mu_list.append(Mutation(individual, "probablistic", prob_list[0], [maybe_i_should_change], arguments=[0.01]))
    if uncertain:
        mu_list.append(Mutation(individual, "probablistic", prob_list[1], [life_is_uncertain]))
    return mu_list

# def mutation_transformation(individual, best_individual, generation, mutations):
#     """
#     Performs a mutation transformation on an individual, given its current generation, the
#     user-configured mutation settings, and a list of mutation dictionaries.

#     Args:
#         individual (object): The individual on which the mutations will be applied.
#         best_individual (object): The current best individual in the population, used for continuous learning.
#         config (dict): The configuration dictionary containing user-configured mutation settings.
#         generation (int): The current generation number of the evolutionary process.
#         mutations (list): List of mutation dictionaries containing mutation types, conditions, and functions.
#     """

#     # Iterate through the list of mutation dictionaries
#     for mutation in mutations:
#         # Conditional Mutation
#         if mutation['type'] == 'conditional':
#             # Check if the condition specified in the mutation dictionary is satisfied
#             if mutation['condition'](individual):
#                 # Apply the mutation function specified in the mutation dictionary
#                 mutation['function'](individual)

#         # Periodic Mutation
#         elif mutation['type'] == 'periodic':
#             # Check if the current generation is a multiple of the period specified in the mutation dictionary
#             if generation % mutation['period'] == 0:
#                 # Apply the mutation function specified in the mutation dictionary with the additional arguments
#                 mutation['function'](individual, *mutation['args'])

#         # Probabilistic Mutation
#         elif mutation['type'] == 'probabilistic':
#             # Check if a random uniform number is less than the probability specified in the mutation dictionary
#             if np.random.uniform() < mutation['probability']:
#                 # Apply the mutation function specified in the mutation dictionary with the additional arguments
#                 mutation['function'](individual, *mutation['args'])

# The main script below is for testing the mutation transformation function with a simple example
# if __name__ == "__main__":
#     # Create two simple ANN models for testing purposes
#     ann1 = SimpleANN([0.1, 0.2, 0.3])
#     ann2 = SimpleANN([0.4, 0.5, 0.6])

#     # Create two individuals for testing purposes
#     individual1 = Individual(1000, 0.5, ann1, [], 'hold')
#     individual2 = Individual(2000, 0.7, ann2, [], 'buy')

#     # Set the best individual
#     best_individual = individual2

#     # Set the current generation
#     generation = 1

#     # Create a list of mutation dictionaries for testing purposes
#     mutations = [
#         {
#             'type': 'conditional',
#             'condition': lambda ind: ind.action == 'hold',
#             'function': emotional_damage,
#         },
#         {
#             'type': 'conditional',
#             'condition': lambda ind: ind.action in ['buy', 'sell'],
#             'function': emotion_okay_lah,
#         },
#         {
#             'type': 'probabilistic',
#             'probability': 0.5,
#             'function': maybe_i_should_change,
#             'args': [0.1],
#         },
#         {
#             'type': 'probabilistic',
#             'probability': 0.3,
#             'function': life_is_uncertain,
#         },
#     ]

#     # Apply mutation transformation to the individual
#     mutation_transformation(individual1, best_individual, generation, mutations)

#     # Print the individual's properties after mutation
#     print("Wallet:", individual1.wallet)
#     print("Emotional resiliency:", individual1.emotional_resiliency)
#     print("ANN weights:", individual1.ann.weights)

#     # Create a simple configuration dictionary for testing purposes
#     config = {
#         'life_is_uncertain_sigma_wallet': 100,
#         'life_is_uncertain_sigma_emotion_resiliency': 1 / 3,
#         'life_is_uncertain_sigma_ann': 0.1,
#     }

#     # Update the 'args' field in the mutation dictionary for the 'life_is_uncertain' mutation function
#     mutations[-1]['args'] = [config]

#     # Apply mutation transformation to the individual again, this time with the updated configuration
#     mutation_transformation(individual1, best_individual, generation, mutations)

#     # Print the individual's properties after the second mutation
#     print("Wallet (after 2nd mutation):", individual1.wallet)
#     print("Emotional resiliency (after 2nd mutation):", individual1.emotional_resiliency)
#     print("ANN weights (after 2nd mutation):", individual1.ann.weights)
