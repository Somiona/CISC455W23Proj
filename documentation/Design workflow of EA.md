# The design workflow of the EA
![[EA_flow.png]]

Components needed:
- Initialization
- Fitness evaluation 
- Actions rundown
- Parent Selection
- Mutation Transformation
- Recombination Transformation 
- Environment Selection (Survivor Selection)
- Termination Condition

## Representation of Individual
In this simulation, individual are investors in the stock market. Each individual will be an object from class Investor
The following are the 7 properties (+1 bonus) each individual will have:
- ID
- Wallet
- ANN model
- Emotion resiliency
- Action
- Current age
- Death age
- Shares_hold
- Journal entry

### Wallet
It represents the liquid asset an individual has currently. 
- Type(Wallet) = Floating point
- Wallet $\in [0, \infty]$
- Individual need cash inside wallet to buy shares of stocks.

### ANN model
It represents the "thinking" of each individual

- Input is previous 30 (time unit) stock price of each stock
- Output value $\in [-1, 1]$
- There are 5 layers: 
	- Input Layer (30 neurons)
	- Hidden Layers 
		- 10 neurons ($K_{30,10}$ mapping)
		- 10 neurons (1-to-1 mapping)
		- 5 neurons  ($K_{10,5}$ mapping)
	- Output Layer (1 neurons, 5x1 mapping)

The current structure of the ANN model (mapping is wrong) is as follow:
![[ann_struct.png]]
image generated from [website](http://alexlenail.me/NN-SVG/index.html) 
![[ann_struct1.png]]
- There are in total of 451 variables for this ANN model
	- Input Layer (30 weights + 30 bias = 60 variables)
	- 1st Hidden Layer (30x10=300 weights + 10 bias = 310 variables)
	- 2nd Hidden Layer (10 weights + 10 bias = 20 variables)
	- 3rd Hidden Layer (10x5=50 weights + 5 bias = 55 variables)
	- Output Layer (5 weights + 1 bias = 6 variables)

- For activation function (subject to change):
	- Use **ReLu** ($f(x)=max(0,x)$) for Input Layer, 1st, 2nd Hidden Layer 
	- Use **Tanh** ($f(x)=\frac{e^x - e^{-x}}{e^x + e^{-x}}$) for the 3rd Hidden Layer and Output Layer

### Emotion resiliency
It represents the desire to purchase/sell the stocks.
It is a boundary value for each individual to decide which one of the following actions will be chosen for this generation: buy, halt (do nothing), and sell 

- Type(Emotion resiliency) = Floating point
- Emotion resiliency $\in [0, 1]$
- Explanation
	- The lower, the higher chance to buy/sell the stock
	- The higher, the higher "self-control"/chance to halt

### Action
It represents the action each individual will perform in this generation
-  **k** action per generation where [k](#hyperparameters) is a hyperparameter
- Type(Action) = \[Encode: Integer, (Stock: String, Price: Floating point), Transaction: Boolean\]
- Action (With encoding):
	- 0 -> Hold (Do nothing for this generation)
	- 1 -> Buy Stock
	- 2 -> Sell Stock
- Transaction is initialized as False

### Age
One of the mechanism for each individual to "die" 

Each Individual will have following properties related to age:
- Current age
	- Everyone starts at 0
	- Increments by 1 after each generation
- Death age
	- Random Normal Distribution from $Normal(75, 10), \mu \;and\; \sigma$ can be adjusted
	- When current age == death age, Individual will perform last action, have a "recombination" with random $k$ individuals to equally share its assets, and remove from the population
- One of the Terminal Conditions
	- Meanwhile an individual dies, the parents will generate one more offspring (introduce new investor) to the population to maintain the population size

### Shares_hold
The amount of stocks each individual holds
- The data type for this property is dictionary
	- {"stock": \[\[First bought stock price, Fail to sell counter\]\]}

### Journal entry
It represents the entire transaction (action) history of each individual throughout the entire simulation

- Type(Journal entry): \[\[\[Action, ("Stock", Price), Transaction status\] x [k](#hyperparameters)\]\]
- Transaction status would be: Success (True), Failed (False)
- 1st layer Index represents the i-th generation
- 2nd layer Index represents which j-th action inside i-th generation


## Decide Action Phrase
![[decide_action.png]]
- Each individual will *randomly order* the stocks and execute the action rundown
- Thus Halt if for all stocks' decision are halt

### Decision condition for Action Selection
The following graph show how each individual decide the action:
![[decide_action.jpg]]
- Individual will perform 
	- Hold if ANN output value $\le$ | emotion resiliency |
	- Buy if ANN output value > emotion resiliency
		- Buy Stocks with price that are lesser than $(1+|ANN\ output|) \times \;average\; of \;previous\; 30\; (time unit)\; stock\; price$
	- Sell if ANN output value < -emotion resiliency
		- Sell Stocks with price $[(1+|ANN output|) \times  average\; of \;previous\; 30\; (time unit)\; stock\; price] \times (1-fail\;to\;sell\;counter/10)$
		- where fail to sell counter starts at 0 and will increment by 1 each generation if no other individual purchase the stock.
		- If sell successfully, that stock's fail to sell counter reset to 0

## Actions Rundown
It simulates the intraday which describe shares that trade on the markets during regular business hours and measure the stock price for this generation.

The following are the steps it run go through:
1. Action decide
2. Intraday trading
3. Update this generation current stocks price
4. Reset action
5. Repeat 1-4 [k](#hyperparameters) times
6. Record this generation stocks closing price

### Action decide
Each individual will [decide](#decide-action-phrase) what action to perform in this generation

### Intraday trading
It simulates the intraday which is tradings on the markets during regular business hours

Thinkings:
- First, we can ignore individuals with Halt action 
- Second, we need a way to *collect* all individual's action and store it to a variable - [Intraday](#intraday)
- Third, we need to iterate every stock and perform a trading algorithm
Trading algorithm:
- Idea: All "buyers" will look on every "seller" share one by one and decide wether buy or not

Pseudo code:
```
def trading(Intraday):
	For stock in all stocks:
		Random shuffle the buy and sell list
		For seller in Intraday[stock][1]: # Sellers
			For buyer in Intraday[stock][0]: # Buyers
				If buyer's price > seller's price:
					buy(buyer, seller)
					# Transaction success and record its price
					Intraday[stock][2].append(seller.action[1])
			if seller.action[2] == False:
				# update failer counter ++
```
```
def buy(buyer, seller, Intraday):
	# Update Seller's properties
	from seller's action find the share it is selling
	remove that share from seller's shares_hold
	add seller's action stock price to seller's wallet
	update buyer's journey entry
	seller's action[2] = True
	# Update Buyer's properties
	add that share to buyer's shares_hold with the new 
```


### Stock Price Update
There are many ways to interpret how a stock price is being defined, here's my *simple* understanding of the meaning of current stock price for a company stock:

**Def**: Current expected stock price per share

and the stock price will change depends on the tradings of individuals, thus the following are the proposed formula for calculating current stock price:
$Current\;Stock\;Price = \frac{\sum_{s=1} ^{S} Success\;Transaction\;Seller's\;Price + (n-s)\times Current\;Stock\;Price}{n}$
- n is the total share amounts of the stock which is fixed when initialization (we are ignoring that the company will expand market share (bonus?))
- S is the total number of success transaction in **1** intraday trading round
- Current Stock Price in the numerator is actually the previous round of stock price which is then being updated
- We will only record the stock price after all [k](#hyperparameters) rounds are finished


##  Global variables
Here are global variables that include in the EA:
- EA general
	- Total generation
	- Current generation (The i value in for loop)
	- Population size
	- Population
- stock market
- Intraday
- A collection of every exist individual (table calendar view ish, bonus)


### Intraday
It collects every individual's action for **one** generation, then will run a function to simulate the *tradings* of that generation, a function to calculate & update this generation's closed stock price, and empty out for next generation

- Type(Intraday) = {"stock": \[\[\Individual with action value has Buy\], \[Individual with action value has Sell\],\[Success transaction\]\]}

#### functions related with Intraday
Here's the list:
- collect_actions()
- trading()
- buy()



## Initialization
Things that need to be initialized :
- Individual
- Stock market

### Individual Initialization


### Stock Market Initialization
It will initialize the amount of company stocks the user want to produce for the simulation.

Theoretically, there are *2* types of individuals holding the stock:
- Shares Directors
	- Directors
	- Mangers
	- Employees
- Normal Investors
	- Uniform distribution

For Shares Directors, they are considered as the CEO of the company, managers or the employees whose hold a portion of company assets.

- It should be **10%** of the population size (maybe hyperparameter to adjust)

For Normal Investors, they are normal people who are interested in investing the stock.

In concept, there are 2 stages for stock to initialize:
- Early Stage
- General Stage

(**shares amount have to be an integer and is recommended to be divisible by 10**)

#### Early Stage
a group of individuals which are the Shares Directors holds 80% of the shares amount, 20% random split to Normal Investors.

Shares Directors' shares distribution (weight is amount of shares they should hold and number is the number of roles that should exists $\frac{role's\;value}{total\; of\;role's\;value = 10}$):
- Directors (weights: 6, number: 4)
- Mangers (weights: 2, number: 3)
- Employees (weights: 2, number: 3)

Default Setting:
Average startup company equity can be considered as $100k, and share amount is 100, thus stock price begins at $100/share

#### General Stage
Generally this is considered post [Series C](https://www.fundz.net/what-is-series-a-funding-series-b-funding-and-more#series-c-funding-2022) of the company, and normally Shares Directors hold **30%** (employees hold 10%, the rest holds 20% [Nasdaq 20 Rule](https://content.next.westlaw.com/practical-law/document/Ibb0a3b6eef0511e28578f7ccc38dcbee/Nasdaq-20-Rule-Stockholder-Approval-Requirements-for-Securities-Offerings?viewType=FullText&originationContext=document&transitionType=DocumentItem&ppcid=0ec041e545d5467096891add2f86ba60&contextData=(sc.DocLink)#:~:text=For%20purposes%20of%20this%20rule,be%20the%20largest%20ownership%20position.) which is Nasdaq generally finds a change of control where an issuance: *Causes a stockholder or stockholder group to own or have the right to acquire 20% or more of the outstanding shares of common stock or voting power*. This ownership or voting power would be the largest ownership position.), 

Shares Directors' shares distribution (weight is amount of shares they should hold and number is the number of roles that should exists $\frac{role's\;value}{total\; of\;role's\;value = 10}$):
- Directors (weights: 5, number: 2)
- Mangers (weights: 3, number: 3)
- Employees (weights: 2, number: 5)

Default Setting:
The mean Series C funding in the U.S. is $72 million, so let's make it easier for calculation, let say $1 million and 10,000 shares which also make the stock price begins at $100/share


## Fitness Function
We come up with **3** different fitness function:
- Asset fitness
- Zero sum fitness
- Potential growth fitness

### Asset fitness
It is considered as a multiple objective fitness function as we are trying to calculate each individual fitness by their assets which we wants to at the same time maximize the liquid asset (cash in the wallet) and the current asset (stock holds value)

The following are the formula:
$asset = \alpha(Wallet) + (1-\alpha)(\#stock\; shares \times current\;stock\;price)$
- $\alpha$ is a hyperparameter

### Zero sum fitness
It is considered a zero sum game where if one individual profits, another individual  loss. It is extended from the asset fitness from above.

The following are the formula:
$zero\;sum=\frac{asset^{(i)}_t - asset^{(i)}_{t-1}}{\frac{1}{n}\sum_{j=1} ^{n} asset^{(j)}_t}$
- $asset^{(i)}_t$ represents the i-th individual's asset at the t-th generation
- The denominator is the average of all individual's asset at the t-th generation

### Potential growth fitness
It is focusing in each individual's growth in assets and would be useful for optimization of finding *best* series of actions or weights of ANN that provide overall highest growth. It is extended from the asset fitness from above.

The following are the formula:
$growth=\frac{asset_t-asset_{t-1}}{asset_{t-1}}$
- $asset^{(i)}_t$ represents the i-th individual's asset at the t-th generation

## Parent Selection
For parent selection, it is a combination of generational and multi-pointer selection.

Since we want to treat a generation as a time interval (day/week/month/year), we are having generational which means all individual will be selected as everyone is experiencing the "new me" replace "old me". 

Multi-pointer selection occurs when an individual reach its death age which means it's throwing away and in order to maintain the fixed population size, we need to perform parent selection.

Our thought is to have a random selection of 2-10 individuals as parents and produce an individual that is "average" of the parents.

As we are introducing a new individual with assets appear out of thin air into the population, it somewhat mimic the inflation and a representation as this EA algorithm as an open system.

For multi-pointer selection, we decide to first rank individuals' assets into 5 classes: low, med-low, medium, med-high, high. Second, based on the pointes, we will random select individuals from the classes.

## Mutation Transformation
For mutation, we have planned out 3 types of mutation: absolute, periodic, and probabilistic.

For each generation, it will run through a series of mutation and we called it a mutation transformation phrase.

Users can decide which mutation will be include inside the series.

### Absolute Mutation
It is a mutation that has a 100% chance to happen for each generation.

The following are a list of absolute mutation that we come up with (bracket indicate what properties are being affected):
- Emotional Damage (emotional resiliency)
- Emotion Okay Lah (emotional resiliency)

#### Emotional Damage
a mutation emphasizing towards the "decrease" of emotion resiliency 

#### Emotion Okay Lah
a mutation emphasizing towards the "increase" of emotion resiliency

### Periodic Mutation
It is a mutation that will occur periodically (every \#n generation)

The following are a list of periodic mutation that we come up with (bracket indicate what properties are being affected):
- get salary (wallet, emotion resiliency)
- pay for survival (wallet, emotion resiliency)
- continuous learning (ANN model)



### Probabilistic Mutation
It is the default setting of mutation where there is a probability to determine if this mutation will be performed

The following are a list of probabilistic mutation that we come up with (bracket indicate what properties are being affected):
- maybe I should change (ANN model)
- life is uncertain (wallet, emotion resiliency, ANN, shares hold)


## Recombination Transformation
For recombination, we have planned out 3 types of recombination: absolute recombination, periodic recombination, and probabilistic recombination.

For each generation, it will run through a series of recombination functions and we called it a recombination transformation phrase.

Users can decide which recombination will be include inside the series.

Also, for recombination functions, there should be 3 levels: crossover, group recombination (2-10 individuals, less than 10% of population), societal recombination (10%-100% of population) 

### Absolute Recombination
It is a recombination that has a 100% chance to happen for each generation.

The following are a list of absolute recombination that we come up with (inside bracket indicate the level and what properties are being affected):
- sharing is caring (crossover: wallet, ANN, shares_hold)
- new investors (group: wallet, ANN, shares_hold)

### Periodic Recombination
It is a recombination that will occur periodically (every \#n generation)

The following are a list of periodic recombination that we come up with (inside bracket indicate the level and what properties are being affected):
- attend lecture (group: wallet, ANN)
- money give it to you (crossover, group, societal: wallet)


### Probabilistic Recombination
There is a probability to determine if this recombination will be performed

The following are a list of  that we come up with (inside bracket indicate the level and what properties are being affected):
- big news (societal: emotion resiliency, wallet, ANN)


## Environment Selection
For environment selection, we decide to use a hybrid version of generational and $(\mu + \lambda)$ where generational adapts the "new me" replace "old me" concept and $(\mu + \lambda)$ for creating new individuals when some of the individuals reach their death age.

There are several ways to deal with "dead" individuals' assets:
- heritage (uniform distribute to a group of individuals)
- straight delete (the assets die with the individual)
- uniform distribution (uniform distribute to every individual)
- lucky guy (an individual will inherit all the asset)

## Termination Condition
For termination condition, it's either reach the generation number or pause anytime (since we are updating the progress per generation) or when every individual halt (hold for more than 3 generations)

## Helper function
The following are helper functions that might be used in any parts of the EA algorithm:
- Random shuffle


## Related to
- [[Document for CISC 455 Project]]
- [[2023-03-20]]