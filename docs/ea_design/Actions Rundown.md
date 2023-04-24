# Actions Rundown
It simulates the intraday which describe shares that trade on the markets during regular business hours and measure the stock price for this generation.

The following are the steps it run go through:
1. Action decide
2. Intraday trading
3. Update this generation current stocks price
4. Reset action
5. Repeat step 1-4 [[Implemented Architecture#Hyperparameters|k]] times
6. Record this generation stocks closing price

## Action decide
Each individual will [decide](#decide-action-phrase) what action to perform in this generation

## Intraday trading
It simulates the intraday which is tradings on the markets during regular business hours

Thinkings:
- First, we can ignore individuals with Halt action
- Second, we need a way to *collect* all individual's action and store it to a variable - [Intraday](#intraday)
- Third, we need to iterate every stock and perform a trading algorithm
Trading algorithm:
- Idea: All "buyers" will look on every "seller" share one by one and decide wether buy or not

Pseudo code:
```python
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

```python
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


## Stock Price Update
There are many ways to interpret how a stock price is being defined, here's my *simple* understanding of the meaning of current stock price for a company stock:

**Def**: Current expected stock price per share

and the stock price will change depends on the tradings of individuals, thus the following are the proposed formula for calculating current stock price:
$Current\;Stock\;Price = \frac{\sum_{s=1} ^{S} Success\;Transaction\;Seller's\;Price + (n-s)\times Current\;Stock\;Price}{n}$
- n is the total share amounts of the stock which is fixed when initialization (we are ignoring that the company will expand market share (bonus?))
- S is the total number of success transaction in **1** intraday trading round
- Current Stock Price in the numerator is actually the previous round of stock price which is then being updated
- We will only record the stock price after all [[Implemented Architecture#Hyperparameters|k]] rounds are finished


