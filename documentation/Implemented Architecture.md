# Implementation Architecture
## Conceptual Architecture
![[455_conceptual_arch.png]]

## Libraries require


## Classes
We uses classes for organization, keep track state, reusability purpose

The following are classes used inside the project:
- Share
- Stock
- Action
- Journal Entry

### Share
It is a **1** unit of share of a stock

Properties:
- ID
- Stock Name
- Price
- Owner
- Owner History

#### ID
Starts with 0


Functions:

## Hyperparameters

Lists for hyperparameters:
k - number of actions for 1 generation (default k=3)
sh_amount - shares amount (fixed) (default sh_amount = 100)
ini_wallet - initial wallet amount for every individual (default ini_wallet = 100)
ini_emo - initial emotion resiliency for every individual (default ini_emo = 0.5)
ini_death - initial death age for every individual (default check [[Design workflow of EA#Representation of Individual#Age|Age]])


## Magic parameters
trend_length - a series number of random stock price before simulation starts (default trend_length = 30)
p_stock_mean - initial stock price mean (default p_stock_mean = 100)
p_stock_sd - initial stock price standard deviation (default p_stock_sd = 30)
p_share_sd - initial share price standard deviation (default p_share_sd = 20)

## Visualization


Things that users can adjust:
- hyperparameters
- Stock Market (Recommend only 2 stocks for quicker computation)
	- Stock Name - String
	- Stock's Shares Amount (Should be less than population size) - Integer
	- Initialization option (Bonus)
		- Random
		- Import an data with 1x30 dimension
- Total Generation 




## Related to
- [[Document for CISC 455 Project]]
- [[2023-03-20]]