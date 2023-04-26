"""
Description: A collection of class representation and initialization methods

Programmer: E Ching Kho
Disclaimer: This is for Queen's University CISC 455 Team Project
            Team member: E Ching Kho, Somoina Tian, Wenqi Tang
            Python Version 3.11.2 when developing
"""
# Import Files and Libraries
import numpy as np
from mutation import mutation_transformation

# Classes
class Share:
    def __init__(self, id, stock, price):
        self.id = id
        self.stock = stock
        self.price = price
        self.owner = None
        self.history = {"price":[], "owner":[]}
        self.failed_selling = 0
    
    def update_history(self):
        """
        Input: None, Output: None
        Record current owner with the share's price into the history
        """
        self.history["price"].append(self.price)
        self.history["owner"].append(self.owner)
        self.failed_selling = 0


    def update_owner(self, investor):
        """
        Input: Investor - investor
        Output: None
        For initalization purpose, to assign share to investor
        """
        self.owner = investor
        investor.shares[self.stock.name].append(self)
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
        return f'{self.stock.name}:{self.id}-($:{self.price},under:{self.owner})'


class Stock:
    def __init__(self, name, num_shares, num_gen, p_stock_mean, p_stock_sd, scope_length, p_share_sd):
        self.name = name
        self.shares = []
        self.num_shares = num_shares
        self.scope_length = scope_length
        self.price_history = np.concatenate((np.round(np.random.normal(p_stock_mean, p_stock_sd, scope_length),2), np.zeros(num_gen))) # Initialize price history wth random trend

        # Generate Shares
        for i in range(num_shares):
            self.shares.append(Share(id=i, stock=self, price=np.round(np.random.normal(self.price_history[scope_length-1], p_share_sd),2))) # shares' price is based on the last tu of random trend

        # Replace last value in the scope
        total_price = 0
        for s in self.shares:
            total_price += s.price
        self.price_history[scope_length-1] = np.round(total_price/num_shares,2)

        # Obtain previous data information
        self.previous_data = self.get_stock_data(0)
        self.average_scope = self.get_average_scope()
        self.last_price = self.price_history[scope_length-1]


    def update_stock(self, curr_gen, price):
        """
        Input: Integer - curr_gen, float - price
        Output: None
        Update information of the stock
        """
        self.price_history[self.scope_length + curr_gen] = price # Update Price
        self.previous_data = self.get_stock_data(curr_gen)
        self.average_scope = self.get_average_scope()


    def get_stock_data(self, curr_gen): 
        """
        Input: Integer - curr_gen
        Output: np.array(Float)
        Get a series of previous tu of stock price
        """
        return self.price_history[curr_gen: curr_gen+self.scope_length]


    def get_average_scope(self):
        return np.average(self.previous_data)

    def get_stock_whole_data(self):
        return self.price_history[self.scope_length:]

    def __repr__(self) -> str:
        return f'S{self.name}-(num:{self.num_shares}, $:{self.last_price})'


class Investor:
    def __init__(self, name, wallet, emotion, death, shares, ann_mean, ann_sd, num_gen):
        self.name = name
        self.wallet = wallet
        self.ann = ANN(ann_mean, ann_sd)
        self.emotion = emotion
        self.action = Action()
        self.current = 1
        self.death = death
        self.shares = shares
        self.time_to_die = False
        self.action_history = np.zeros(num_gen)
        self.action_value = None
        self.mutation_list = mutation_transformation(self,[0.33,0.1],None,num_gen,[5,10,0],[10,10,0], True, True, True, False, True, True)
    

    def aging(self):
        """
        Input: None, Output: None
        update the investor current age and check if the investor reaches its death age
        """
        self.current += 1
        self.time_to_die = self.current == self.death

    def add_wallet(self, value):
        self.wallet += value
        self.wallet = 0 if self.wallet <= 0 else self.wallet

    def add_emotion(self, value):
        self.emotion += value
        if not 0 <= self.emotion <= 1:
            if self.emotion <= 0:
                self.emotion = 0
            else: # >= 1
                self.emotion = 1

    def record_action(self, curr_gen, action):
        """
        Input: Integer - curr_gen, Integer - action
        Output: None
        Description: action meaning - {"halt": 0, "buy": 1, "sell": -1}
        """
        self.action_history[curr_gen] += action

    def get_action_value(self, curr_gen):
        self.action_value = self.action_history[curr_gen]

    def decide_action(self, market, curr_gen):
        """
        Input: [Stock] - market, Integer - curr_gen
        Output: None
        Description: Decide Action
        """
        np.random.shuffle(market) # So that every individual will have different order

        for stock in market:
            val = self.ann.predict(stock.previous_data) # Predict based on scope of previous data of the stock
            # print(val)
            if -self.emotion <= val <= self.emotion: # Halt for this stock
                continue
            else:
                if val > self.emotion: # Buy this stock
                    if stock.average_scope * (1 + abs(val)) >= self.wallet:
                        self.action.set_action(1, self.wallet, stock_name=stock.name)
                        self.record_action(curr_gen, 1)
                    else:
                        self.action.set_action(1, stock.average_scope * (1 + abs(val)), stock_name=stock.name)
                        self.record_action(curr_gen, 1)
                    return # Since we decide to Buy already
                else:
                    # Sell
                    if self.shares[stock.name]:
                        share = np.random.choice(self.shares[stock.name])
                        self.action.set_action(2, (1 + abs(val)) * share.price * (1-share.failed_selling/10), stock_share=share)
                        self.record_action(curr_gen, -1)
                        return # Since we decide to Sell already
                    else:
                        # no shares...
                        continue
        # Since all stocks are halt thus this action is halt
        self.action.set_action(0)
        self.record_action(curr_gen, 0)

    def mutate(self):
        for mutation in self.mutation_list:
            mutation.decide_function()

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
    layer_name = ["input_weights","input_biases", "hidden_weights", "hidden_biases", "output_weights", "output_bias"]

    def __init__(self, mean=0, sd=0.1):
        self.input_weights = np.random.normal(mean,sd,30)
        self.input_biases = np.random.normal(mean,sd,30)
        self.hidden_weights = np.random.normal(mean,sd,(30, 10))
        self.hidden_biases = np.random.normal(mean,sd,10)
        self.output_weights = np.random.normal(mean,sd,10)
        self.output_bias = np.random.normal(mean,sd)
        self.total_weights = (self.input_weights.size + self.input_biases.size + self.hidden_weights.size + self.hidden_biases.size + self.output_weights.size + 1) # +1 for the output bias

    def predict(self, input_values):
        input_layer = np.maximum(input_values * self.input_weights + self.input_biases, 0) # ReLu()
        hidden_layer = np.maximum(input_layer @ self.hidden_weights + self.hidden_biases, 0) # ReLu()
        # input_layer = np.tanh(input_values * self.input_weights + self.input_biases) # tanh()
        # hidden_layer = np.tanh(input_layer @ self.hidden_weights + self.hidden_biases) # tanh()
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
            }

    def add_weight(self, index, value):
        weight, pos = self._get_weight_by_index(index)
        if isinstance(pos, tuple):
            i, j = pos
            weight[i, j] += value
        else:
            weight[pos] += value

    def add_weights(self, indices, values):
        for index, value in zip(indices, values):
            self.add_weight(index, value)


    def add_everything(self, values):
        self.input_weights += values["input_weights"]
        self.input_biases += values["input_biases"]
        self.hidden_weights += values["hidden_weights"]
        self.hidden_biases += values["hidden_biases"]
        self.output_weights += values["output_weights"]
        self.output_bias += values["output_bias"]


    def add_all_weights(self, value):
        for i in range(381):
            self.add_weight(i, value)

    def update_weight(self, index, value):
        weight, pos = self._get_weight_by_index(index)
        if isinstance(pos, tuple):
            i, j = pos
            weight[i, j] = value
        else:
            weight[pos] = value

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
            return [self.output_bias], 0
        raise IndexError("Invalid weight index")


class Action():
    encode = {0: "halt", 1: "buy", 2: "sell", None: "None"}

    def __init__(self):
        self.action_num = None
        self.transaction = False
        self.price = None
        self.stock_share = None
        self.stock_name = None
        self.stock_index = None
    

    def set_action(self, action, price=None, stock_share=None, stock_name=None):
        """
        Input: Integer - action, Float - price, Share - stock_share, String - stock_name
        Output: None
        Set action
        """
        self.action_num = action
        if action == 0 and stock_share != None and price != None:
            print("ERROR: action is Hold but stock and price are inputted")
        else:
            if action != 0:
                self.price = np.round(price,2)
                if action == 1:
                    self.stock_name = stock_name
                elif action == 2:
                    self.stock_share = stock_share


    def reset(self):
        self.action_num = None
        self.transaction = False
        self.price = None
        self.stock_share = None
        self.stock_name = None
        self.stock_index = None


    def __str__(self) -> str:
        return f'A-{self.encode[self.action_num]}({"sell:$" + str(self.price) + ", share:"+ str(self.stock_share) + "," if self.action_num==2 else "ub:$" + str(self.price) + "," + "stock:" + self.stock_name + "," if self.action_num == 1 else "" if self.action_num != None else ""}{"T" if self.transaction else "F"})'

    def __repr__(self) -> str:
        return f'A-{self.encode[self.action_num]}(price:{self.price},stock_name:{self.stock_name},share:{self.stock_share},{"T" if self.transaction else "F"})'


def initialize_investors(stock_names, num_ind, wallet=200, emotion=0.5, death_mean=75, death_sd=10, ann_mean=0, ann_sd=0.4, num_gen=100):
    """
    Input: Integer - num_ind, Float - wallet, Float - emotion, Integer - death_mean, Integer - death_sd, [String] - stock_names
    Output: np.Array(Investor)
    Initialize Investors
    """
    investors = [Investor(i, wallet, emotion, int(np.random.normal(death_mean, death_sd)), {name: [] for name in stock_names}, ann_mean, ann_sd, num_gen) for i in range(num_ind)]
    return np.array(investors)


def initialize_stock(num_stocks=2, num_shares=100, num_gen=100, names=["ABC","XYZ"], p_stock_mean=100, p_stock_sd=20, scope_length=30, p_share_sd=10):
    """
    Input: Integer - num_stocks
    Optional Inputs: Integer - num_shares, Integer - num_gen, [String] - names, Integer - p_stock_mean, Integer - p-stock_sd, Integer - scope_length, Integer - p_share_sd
    Output: np.array(Stock)
    Initialize Stocks
    """
    if len(names) == 0:
        stocks = [Stock(i, num_shares, num_gen, p_stock_mean, p_stock_sd, scope_length, p_share_sd) for i in range(num_stocks)]
    else:
        if len(names) == num_stocks:
            stocks = [Stock(i, num_shares, num_gen, p_stock_mean, p_stock_sd, scope_length, p_share_sd) for i in names] # len(names) == num_stocks should be true
        else:
            print("ERROR: The length of names and num_stocks doesn't match!!!")
            stocks = [Stock(i, num_shares, num_gen, p_stock_mean, p_stock_sd, scope_length, p_share_sd) for i in range(num_stocks)]
    return np.array(stocks)


def assign_initial_shares(investors, stocks, num_directors, stage_threshold):
    """
    Input: np.Array(Investor) - investors, np.Array(Investor) - stocks, Integer - stage_threshold
    Output: None
    Assign shares of stock to investors based on the provided stage
    """
    for stock in stocks:
        # Shuffle the array randomly
        np.random.shuffle(stock.shares)
        np.random.shuffle(investors)

        if stock.num_shares <= stage_threshold: # early stage
            directors_share_ratio = 0.8
            
        else: # general stage
            directors_share_ratio = 0.3

        # Get Directors Shares and Normal Investors Shares
        directors_size = int(np.round(directors_share_ratio * stock.num_shares))
        directors_shares = stock.shares[:directors_size]
        normal_shares = stock.shares[directors_size:]

        # Get Investors as directors and Normal Investors
        directors = investors[:num_directors]
        normal_inv = investors[num_directors:]

        # Assign Directors Shares, Normal Investors Shares to directors, normal investors respectively
        for share in directors_shares:
            share.update_owner(np.random.choice(directors))

        for share in normal_shares:
            share.update_owner(np.random.choice(normal_inv))


### Test ANN ###
# net = ANN(0,0.3)
# print(net.get_weights()) # test get_weights()
# print(net.get_weights(False)) # test get_weights()

### test predict() # Basically ANN sd should be < 0.2
# for i in range(10):
#     net = ANN(0,0.1)
#     input_values = np.random.normal(100,30,30)
#     # print(input_values)
#     print(net.predict(input_values))

### test get_weight(), add_weight(), and update_weight()
# print("10th weight is: " + str(net.get_weight(10)))
# print(str(net.get_weight(10)) + " + 5 = " + str(net.get_weight(10) + 5))
# net.add_weight(10, 5)
# print("10th weight is: " + str(net.get_weight(10)))
# net.update_weight(10, 22)
# print("10th weight is: " + str(net.get_weight(10)))

### test add_weights(self, indices, values)
# print(net.get_weights(False)) # test get_weights()
# net.add_weights([1,3,5,7,9], [10,20,30,40,50])
# print(net.get_weights(False)) # test get_weights()

### Test Investor's aging###
# arron = Investor(1, 100, 0.5, 3, {}, 0,0.1)
# print(repr(arron))
# arron.aging()
# print(repr(arron))
# arron.aging()
# print(repr(arron))

### Test Stock ###
# abc = Stock("ABC", 20, 50, 100,20, 30, 10)
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
# population = initialize_investors(["ABC"],50, 100.0, 0.3, 75, 5)
# print(population)

### Test initialize_stock() ###
# market = initialize_stock(num_stocks=2, num_shares=20, num_gen=20, names=["ABC", "XYZ"])
# # market = initialize_stock()
# for stock in market:
#     print(stock)
#     print(stock.shares)
#     print(stock.price_history)

### Test assign_initial_shares ###
# names = ["ABC", "XYZ"]
# population = initialize_investors(names,50, 100.0, 0.5, 75, 5)
# market = initialize_stock(num_stocks=2, num_shares=20, num_gen=20, names=names)
# assign_initial_shares(population, market, 5, 20)
# for stock in market:
#     print(stock)
#     for i in stock.shares:
#         print(i)
#     print()
# for i in population:
#     print(repr(i))

### Test Action ###
# act = Action()
# print(act)
# s0 = Stock('ABC', num_shares=1, num_gen=20, p_stock_mean=100, p_stock_sd=1, scope_length=30, p_share_sd=1)

# act.set_action(0, stock_share=s0.shares[0], price=50)
# act.set_action(0)
# print(act)
# act.set_action(2, 100, stock_share=s0.shares[0]) # sell
# print(act)
# act.set_action(1, price=200, stock_name=s0.name) # buy
# print(act)
# act.reset()
# print(act)

### Test update_price in Stock and get_stock_data ###
# market = initialize_stock(1, 5, 30, ["ABC"])
# s0 = market[0]
# print(s0.price_history)
# s0.update_stock(0, 10.0)
# s0.update_stock(1, 20.0)
# print(s0.price_history)
# print(s0.previous_data)
# print(s0.previous_data.shape)
# print(s0.average_scope)

### Test Decide Action ###
# market_names = ["ABC", "XYZ"]
# market = initialize_stock(2, 10, 20, market_names)
# population = initialize_investors(market_names,10, 500, 0.5, 75, 10)
# assign_initial_shares(population, market, 2, 1)

# for ind in population:
#     print(repr(ind))
#     print(ind.action)
# print()
# print("Decide Action")
# for ind in population:
#     ind.decide_action(market)
#     print(repr(ind))
#     print(ind.action)

