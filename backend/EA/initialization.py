"""
Description: A collection of class representation and initialization methods

Programmer: E Ching Kho
Disclaimer: This is for Queen's University CISC 455 Team Project
            Team member: E Ching Kho, Somoina Tian, Wenqi Tang
            Python Version 3.11.2 when developing
"""
# Import Files and Libraries
import numpy as np

# Classes
class Share:
    def __init__(self, id, stock, price):
        self.id = id
        self.stock = stock
        self.price = price
        self.owner = None
        self.history = {"price":[], "owner":[]}
    
    def update_history(self):
        """
        Input: None, Output: None
        Record current owner with the share's price into the history
        """
        self.history["price"].append(self.price)
        self.history["owner"].append(self.owner)

    def update_owner(self, investor):
        """
        Input: Investor - investor
        Output: None
        For initalization purpose, to assign share to investor
        """
        self.owner = investor
        investor.shares.append(self)
        self.update_history()


    def update_owner_price(self, owner, price):
        """
        Input: Investor - investor, Float - price
        Output: None
        Update the owner and share's price
        """
        self.owner = owner
        self.price = price
        self.update_history()

    def __repr__(self) -> str:
        return f'{self.stock.id}:{self.id}-($:{self.price},under:{self.owner})'


class Stock:
    def __init__(self, id, num_shares, num_gen, p_stock_mean, p_stock_sd, trend_length, p_share_sd):
        self.id = id
        self.shares = []
        self.num_shares = num_shares
        self.price_history = np.concatenate((np.random.normal(p_stock_mean, p_stock_sd, trend_length), np.zeros(num_gen))) # Initialize price history wth random trend

        # Generate Shares
        for i in range(num_shares):
            self.shares.append(Share(id=i, stock=self, price=np.random.normal(self.price_history[trend_length-1], p_share_sd))) # shares' price is based on the last tu of random trend

        # Replace last trend value
        total_price = 0
        for s in self.shares:
            total_price += s.price
        self.price_history[trend_length-1] = total_price/num_shares


    def __repr__(self) -> str:
        return f'S{self.id}-(num:{self.num_shares})'


class Investor:
    def __init__(self, name, wallet, emotion, death):
        self.name = name
        self.wallet = wallet
        self.ann = ANN()
        self.emotion = emotion
        self.current = 1
        self.death = death
        self.shares = []
        self.time_to_die = False
    
    def aging(self):
        """
        Input: None, Output: None
        update the investor current age and check if the investor reaches its death age
        """
        self.current += 1
        self.time_to_die = self.current == self.death

    def __str__(self) -> str:
        return f'I{self.name}'

    def __repr__(self) -> str:
        return f'I{self.name}-(w:{self.wallet},emo:{self.emotion},age:{self.current},death:{self.death},ttd:{self.time_to_die},shares:{self.shares})'


class ANN():
    '''
    Class ANN represents the "thinking" of each investor
    
    Functions:
    predict(input_values), get_weight(index), get_weights(dim:bool), add_weight(index, value), add_weights(indices, values),
    add_all_weights(value), update_weight(index, value)

    Index position:
    0 to 29: Input layer weights
    30 to 59: Input layer biases
    60 to 359: Hidden layer weights
    360 to 369: Hidden layer biases
    370 to 379: Output layer weights
    380: Output layer bias

    weights and bias are initalized using Standard Normal Distribution (https://numpy.org/doc/stable/reference/random/generated/numpy.random.randn.html)
    '''
    def __init__(self):
        self.input_weights = np.random.randn(30)
        self.input_biases = np.random.randn(30)
        self.hidden_weights = np.random.randn(30, 10)
        self.hidden_biases = np.random.randn(10)
        self.output_weights = np.random.randn(10)
        self.output_bias = np.random.randn()
        self.total_weights = (self.input_weights.size + self.input_biases.size + self.hidden_weights.size + self.hidden_biases.size + self.output_weights.size + 1) # +1 for the output bias

    def predict(self, input_values):
        input_layer = np.maximum(input_values * self.input_weights + self.input_biases, 0) # ReLu()
        hidden_layer = np.maximum(input_layer @ self.hidden_weights + self.hidden_biases, 0) # ReLu()
        output_layer = np.tanh(hidden_layer @ self.output_weights + self.output_bias) # Tanh()
        return output_layer
    
    def get_weight(self, index):
        weight, i = self._get_weight_by_index(index)
        return weight[i]

    def get_weights(self, dim=True):
        if dim:
            return {
            "input_weights": self.input_weights.shape,
            "input_biases": self.input_biases.shape,
            "hidden_weights": self.hidden_weights.shape,
            "hidden_biases": self.hidden_biases.shape,
            "output_weights": self.output_weights.shape,
            "output_bias": 1,
            "total weights & bias": self.total_weights
        }
        else:
            return {
                "input_weights": self.input_weights,
                "input_biases": self.input_biases,
                "hidden_weights": self.hidden_weights,
                "hidden_biases": self.hidden_biases,
                "output_weights": self.output_weights,
                "output_bias": self.output_bias,
                "total weights & bias": self.total_weights
            }

    def add_weight(self, index, value):
        weight, i = self._get_weight_by_index(index)
        weight[i] += value

    def add_weights(self, indices, values):
        for index, value in zip(indices, values):
            self.add_weight(index, value)

    def add_all_weights(self, value):
        for i in range(381):
            self.add_weight(i, value)

    def update_weight(self, index, value):
        weight, i = self._get_weight_by_index(index)
        weight[i] = value

    def _get_weight_by_index(self, index):
        if 0 <= index <= 29:
            return self.input_weights, index
        index -= 30
        if 0 <= index <= 29:
            return self.input_biases, index
        index -= 30
        if 0 <= index <= 299:
            i, j = divmod(index, 10)
            return self.hidden_weights[i], j
        index -= 300
        if 0 <= index <= 9:
            return self.hidden_biases, index
        index -= 10
        if 0 <= index <= 9:
            return self.output_weights, index
        index -= 10
        if index == 0:
            return self.output_bias, 0
        raise IndexError("Invalid weight index")


def initialize_investors(num_ind, wallet, emotion, death_mean, death_sd):
    """
    Input: Integer - num_ind, Float - wallet, Float - emotion, Integer - death_mean, Integer - death_sd
    Output: np.Array(Investor)
    Initialize Investors
    """
    investors = [Investor(i, wallet, emotion, int(np.random.normal(death_mean, death_sd))) for i in range(num_ind)]
    return np.array(investors)


def initialize_stock(num_stocks=2, num_shares=100, num_gen=100, names=[], p_stock_mean=100, p_stock_sd=20, trend_length=30, p_share_sd=20):
    """
    Input: Integer - num_stocks
    Optional Inputs: Integer - num_shares, Integer - num_gen, [String] - names, Integer - p_stock_mean, Integer - p-stock_sd, Integer - trend_length, Integer - p_share_sd
    Output: np.array(Stock)
    Initialize Stocks
    """
    if len(names) == 0:
        stocks = [Stock(i, num_shares, num_gen, p_stock_mean, p_stock_sd, trend_length, p_share_sd) for i in range(num_stocks)]
    else:
        if len(names) == num_stocks:
            stocks = [Stock(i, num_shares, num_gen, p_stock_mean, p_stock_sd, trend_length, p_share_sd) for i in names] # len(names) == num_stocks should be true
        else:
            print("ERROR: The length of names and num_stocks doesn't match!!!")
            stocks = [Stock(i, num_shares, num_gen, p_stock_mean, p_stock_sd, trend_length, p_share_sd) for i in range(num_stocks)]
    return np.array(stocks)


def assign_initial_shares(investors, stocks, num_directors, stage="general"):
    """
    Input: np.Array(Investor) - investors, np.Array(Investor) - stocks, String - stage
    Output: None
    Assign shares of stock to investors based on the provided stage
    """
    for stock in stocks:
        # Shuffle the array randomly
        np.random.shuffle(stock.shares)
        np.random.shuffle(investors)

        if stage == "early":
            directors_ratio = 0.8
            dir_share_ratio = 0.6
            man_share_ratio = 0.2
            dir_num_ratio = 0.4
            man_num_ratio = 0.3 + dir_num_ratio
        else:
            # stage == "general"
            if stage != "general":
                print("ERROR: initialization stage should be general or early")
            directors_ratio = 0.3
            dir_share_ratio = 0.5
            man_share_ratio = 0.3
            dir_num_ratio = 0.2
            man_num_ratio = 0.3 + dir_num_ratio

        # Assign shares to the directors investors
        # Get different Directors Share's Size
        directors_size = int(directors_ratio * len(stock.shares))
        dir_size = int(dir_share_ratio * directors_size)
        man_size = int(man_share_ratio * directors_size)
        emp_size = directors_size - dir_size - man_size

        # Get Investors as directors
        directors = np.random.choice(len(investors), num_directors, replace=False)
        num_dir = len(directors) # default should be 10% of total number of investors
        dir_investors = investors[directors[:int(dir_num_ratio * num_dir)]]
        man_investors = investors[directors[int(dir_num_ratio * num_dir): int(man_num_ratio * num_dir)]]
        emp_investors = investors[directors[int(man_num_ratio * num_dir):]]

        # Get different Directors Shares
        dir_shares = stock.shares[:dir_size]
        man_shares = stock.shares[dir_size:dir_size+man_size]
        emp_shares = stock.shares[dir_size+man_size:dir_size+man_size+emp_size]

        # Assign
        for share in dir_shares:
            share.update_owner(np.random.choice(dir_investors))
        for share in man_shares:
            share.update_owner(np.random.choice(man_investors))
        for share in emp_shares:
            share.update_owner(np.random.choice(emp_investors))
        
        
        # Assign shares to the normal investors (uniformly distributed)
        normal_shares = stock.shares[directors_size:] # Get shares for normal investors
        normal_investors = investors[np.setdiff1d(np.arange(len(investors)),directors)] # Get normal investors

        for share in normal_shares:
            share.update_owner(np.random.choice(normal_investors))


"""Test cases
forward(input_values), get_weights(), add_weight(index, value), add_weights(indices, values),
add_all_weights(value), update_weight(index, value)
"""
### Test ANN ###
# net = ANN()
# print(net.get_weights()) # test get_weights()
# print(net.get_weights(False)) # test get_weights()

### test predict()
# input_values = [*range(1,31)]
# input_values = np.random.randn(30) # maybe all layers use tanh is better?
# print(input_values)
# output = net.predict(input_values)
# print(output)

### test get_weight(), add_weight(), and update_weight()
# print("10th weight is: " + str(net.get_weight(10)))
# print(str(net.get_weight(10)) + " + 5 = " + str(net.get_weight(10) + 5))
# net.add_weight(10, 5)
# print("10th weight is: " + str(net.get_weight(10)))
# net.update_weight(10, 22)
# print("10th weight is: " + str(net.get_weight(10)))

### Test Investor ###
# arron = Investor(1, 100, 0.5, 3)
# print(arron)
# arron.aging()
# print(arron)
# arron.aging()
# print(arron)

### Test Stock ###
# abc = Stock("ABC", 20, 50)
# print(abc)
# print(abc.shares)
# print(len(abc.shares))
# print(abc.price_history)

### Test Share ###
# xyz = Stock("XYZ", 20, 50)
# s0 = xyz.shares[0]
# print(s0)
# s0.update_owner_price("John", 100)
# print(s0)
# print(s0.history)

### Test initialize_investors() ###
# population = initialize_investors(50, 100.0, 0.5, 75, 5)
# print(population)

### Test initialize_stock() ###
# market = initialize_stock(num_stocks=2, num_shares=20, num_gen=20, names=["ABC", "XYZ"])
# # market = initialize_stock()
# for stock in market:
#     print(stock)
#     print(stock.shares)
#     print(stock.price_history)

### Test assign_initial_shares ###
# population = initialize_investors(50, 100.0, 0.5, 75, 5)
# market = initialize_stock(num_stocks=2, num_shares=20, num_gen=20, names=["ABC", "XYZ"])
# assign_initial_shares(population, market, 10, "early")
# for stock in market:
#     print(stock)
#     print(len(stock.shares))
#     for i in stock.shares:
#         print(i)
#     print()
# for i in population:
#     print(repr(i))