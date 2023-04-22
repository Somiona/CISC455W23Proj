"""
A collection of class representation and initialization methods

Student number: E Ching Kho (Noon Kho) (He/him)
Student name: 20118077
Disclaimer: Python Version I use is 3.11.2
"""
# To to be imported
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
        self.history["price"].append(self.price)
        self.history["owner"].append(self.owner)

    def update_owner_price(self, owner, price):
        self.owner = owner
        self.price = price

    def __repr__(self) -> str:
        return f'{self.stock.id}:{self.id}($:{self.price},under:{self.owner})'


class Stock:
    def __init__(self, id, num_shares, p_stock_mean=100, p_stock_sd=30, trend_length=30, p_share_sd=20):
        self.id = id
        self.shares = []
        self.num_shares = num_shares
        self.price_history = np.random.normal(p_stock_mean, p_stock_sd, trend_length) # Generate random trend

        # Generate Shares
        for i in range(num_shares):
            self.shares.append(Share(id=i, stock=self, price=np.random.normal(self.price_history[-1], p_share_sd)))

        # Replace last trend value
        total_price = 0
        for s in self.shares:
            total_price += s.price
        self.price_history[-1] = total_price/num_shares

        
    def __repr__(self) -> str:
        return f'S-{self.id}(num:{self.num_shares})'




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
        self.current += 1
        self.time_to_die = self.current == self.death

    def __repr__(self) -> str:
        return f'Investor-{self.name}(w:{self.wallet},emo:{self.emotion},age:{self.current},death:{self.death},ttd:{self.time_to_die},shares:{self.shares})'


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

### Test Share ###


### Test Stock
