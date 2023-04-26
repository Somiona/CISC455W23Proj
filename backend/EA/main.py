"""
Description: Evolutionary Algorithm

Programmer: 
Disclaimer: This is for Queen's University CISC 455 Team Project
            Team member: E Ching Kho, Somoina Tian, Wenqi Tang
            Python Version 3.11.2 when developing
"""
# Import Files and Libraries
import numpy as np
from initialization import initialize_investors, initialize_stock, assign_initial_shares
from evaluation import asset_fitness
from parent_selection import ranking, rank_pointer_selection, random_pair
from recombination import teach_me_something_bro
import matplotlib.pyplot as plt

def ea(pop_size, wallet, emotion, death_mean, death_sd, num_directors, market_names, num_shares, num_gen, k, fitness_alpha, recom_alpha, recom_beta):
    """
    Input: Integer - pop_size, Float - wallet, Float - emotion, Integer - death_mean, Integer - death_sd, Integer - num_directors, [String] - market_names, Integer - num_shares, Integer - num_gen, Integer - k, Float - fitness_alpha, Float - recom_alpha, Float - recom_beta
    Output: [Stock]
    Description: Stock Simulation Evolutionary Algorithm
    """
    # Initialization
    market = initialize_stock(len(market_names),num_shares, num_gen, market_names)
    population = initialize_investors(market_names, pop_size, wallet, emotion, death_mean, death_sd)
    assign_initial_shares(population, market, num_directors, 8)
    
    # Loop
    for curr_gen in range(num_gen):
        # Action Rundown
        action_rundown(k, population, market, curr_gen)

        # Fitness evaluation (Future Work)
        # fitness = []
        # for ind in population:
        #     fitness.append(asset_fitness(ind, fitness_alpha))

        # Parent selection
        parents = random_pair(population)

        # Mutation Transformation
        for ind in population:
            ind.mutate()
        
        # Recombination Transformation
        for (ind1, ind2) in parents:
            teach_me_something_bro(ind1, ind2, recom_alpha, recom_beta)
        
        # Generate Offspring (Future Work)

        # Environment Selection (Future Work)

    return market


def get_stock_names(market):
    """
    Input: [Stock] - market
    Output: [String]
    Get All Stock name in the market
    """
    names = []
    for stock in market:
        names.append(stock.name)
    return names


def action_rundown(k, population, market, curr_gen):
    for _ in range(k):
        # Action Decide
        for ind in population:
            ind.decide_action(market, curr_gen)

        # for ind in population:
        #     print(ind.action)
        # for ind in population:
        #     print(ind.emotion)

        # Intraday Trading
        transactions = intraday_trading(population, get_stock_names(market))
        # print(transactions)
        # Update Stock's last price
        for stock in market:
            stock.last_price = np.round((np.sum(transactions[stock.name]) + (stock.num_shares - len(transactions[stock.name]))*stock.last_price)/stock.num_shares,2)
        # Reset Every Indivdual's Action (Just in case even though it replaces the previous action)
        for ind in population:
            ind.action.reset()
    
    # Record this generation stocks closing price
    for stock in market:
        stock.update_stock(curr_gen, stock.last_price)


def intraday_trading(population, market_names):
    intraday = {stock: [[],[]] for stock in market_names} # {"stock": [[],[]]} index 0 is Individual who Buy, index 1 is Individual who Sell 
    transactions = {stock: [] for stock in market_names} # Store Success Transactions' Sold Price
    
    # Collect Individual based on Action
    for ind in population:
        if ind.action.action_num != 0:
            if ind.action.action_num == None:
                print("ERROR: action shouldn't be None")
            else:
                if ind.action.action_num == 1: # Indivdual with Buy Action
                    intraday[ind.action.stock_name][0].append(ind)
                elif ind.action.action_num == 2: # Indivdual with Sell Action
                    intraday[ind.action.stock_share.stock.name][1].append(ind)
                else:
                    print("ERROR: action encoding should be just 0,1,2")

    # Trading
    for stock, value in intraday.items():
        if value[1]: # There exists Seller
            np.random.shuffle(value[0]) # Random Shuffle Buyer list
            seller_price = [seller.action.price for seller in value[1]]
            for buyer in value[0]:
                if buyer.action.price >= np.min(seller_price): # Investor is smart and buy the cheapest available
                    # Transaction success and record the sold price
                    seller_index = np.argmin(seller_price)
                    transactions[stock].append(buy(buyer, value[1][seller_index]))
                    del value[1][seller_index] # remove from Seller list
                    del seller_price[seller_index] # remove from seller_price list
                    if not seller_price:
                        break # no more individual selling

            # Failed Selling++ for those remaining Sellers who can't sell
            for seller in value[1]:
                seller.action.stock_share.failed_selling += 1
    
    return transactions


def buy(buyer, seller):
    """
    Input: Investor - buyer, Investor - seller
    Output: float
    Perform the transaction action between buyer and seller and Return the sold price
    """
    share = seller.action.stock_share # Get the share that are trading

    # Trade Share
    seller.shares[share.stock.name].remove(share) # Remove Share from Seller
    buyer.shares[share.stock.name].append(share)

    # Trade Money
    sold_price = seller.action.price
    seller.wallet += sold_price
    buyer.wallet -= sold_price

    # Update share's owner
    share.update_owner_price(buyer, sold_price)

    # Update Transaction's Status
    seller.action.transaction = True
    buyer.action.transaction = True

    return sold_price


### Test buy() ###
# print("initialize")
# pop = initialize_investors(["ABC"], 2, 50)
# print(pop)
# mar = initialize_stock(1, 1, 20, ["ABC"], 20, 2, 5, 1)
# share = mar[0].shares[0] # share
# print(share)
# share.update_owner(pop[0])
# print("assigned")
# print(pop)
# print(share)
# pop[0].action.set_action(2, 20, stock_share=share)
# pop[1].action.set_action(1, 25, stock_name="ABC")
# print(pop[0].action)
# print(pop[1].action)
# print("buy")
# print("sold price:" + str(buy(pop[1], pop[0])))
# print(pop)
# print(share.history)
# print(pop[0].action)
# print(pop[1].action)


### Test Action Rundown
# market_names = ["ABC", "XYZ"]
# market = initialize_stock(2, 5, 20, market_names)
# population = initialize_investors(10, 100, 0.5, 75, 10, market_names)
# curr_gen = 0
# assign_initial_shares(population, market, 2)

### Test ea
market = ea(50, 200.0, 0.1, 100, 0, 5, ["ABC","XYZ"], 100, 100, 3, 0.5, 0.05, 0.05)
for stock in market:
    # plt.figure()
    # plt.plot(np.arange(100), stock.get_stock_whole_data())
    # plt.title("Stock " + stock.name + " Price")
    # plt.xlabel("Generation")
    # plt.ylabel("Price Data")
    # plt.savefig(stock.name + ".png")

    plt.plot(np.arange(100), stock.get_stock_whole_data())
    plt.title("Stock Simulation")
    plt.xlabel("Generation")
    plt.ylabel("Price Data")
    plt.legend(["ABC","XYZ"])
    plt.savefig(stock.name + ".png")