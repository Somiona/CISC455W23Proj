# Initialization
Things that need to be initialized :
- Individual
- Stock market

## Individual Initialization
It will initialize every individual's properties value:
- name (it will be number sadly)
- wallet ([[Implemented Architecture#Hyperparameters|ini_wallet]])
- ANN (every weight and bias is random number from standard normal distribution)
- emotional resiliency ([[Implemented Architecture#Hyperparameters|ini_emo]])
- current age (everyone is 1)
- death age (ini_death)
- shares_hold (check below Stock Market Initialization)

## Stock Market Initialization
It will initialize the stock market based on the user's input

For each stock, it will process 3 steps:
1. Generate 30 (tu) ([[Implemented Architecture#Magic parameters|trend_length]]) of stock price with Normal[[Implemented Architecture#Magic parameters|(p_stock_mean, p_stock_sd)]]
2. Generate the given amount of shares ([[Implemented Architecture#Hyperparameters|sh_amount]]) with price Normal(30th tu of stock price, [[Implemented Architecture#Magic parameters|p_share_sd]])
3. Update the 30th (tu) stock price with average of shares price
4. shares assign to individuals

## Step 3
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

### Early Stage
a group of individuals which are the Shares Directors holds 80% of the shares amount, 20% random split to Normal Investors.

Shares Directors' shares distribution (weight is amount of shares they should hold and number is the number of roles that should exists $\frac{role's\;value}{total\; of\;role's\;value = 10}$):
- Directors (weights: 6, number: 4)
- Mangers (weights: 2, number: 3)
- Employees (weights: 2, number: 3)

Default Setting:
Average startup company equity can be considered as $100k, and share amount is 100, thus stock price begins at $100/share

### General Stage
Generally this is considered post [Series C](https://www.fundz.net/what-is-series-a-funding-series-b-funding-and-more#series-c-funding-2022) of the company, and normally Shares Directors hold **30%** (employees hold 10%, the rest holds 20% [Nasdaq 20 Rule](https://content.next.westlaw.com/practical-law/document/Ibb0a3b6eef0511e28578f7ccc38dcbee/Nasdaq-20-Rule-Stockholder-Approval-Requirements-for-Securities-Offerings?viewType=FullText&originationContext=document&transitionType=DocumentItem&ppcid=0ec041e545d5467096891add2f86ba60&contextData=(sc.DocLink)#:~:text=For%20purposes%20of%20this%20rule,be%20the%20largest%20ownership%20position.) which is Nasdaq generally finds a change of control where an issuance: *Causes a stockholder or stockholder group to own or have the right to acquire 20% or more of the outstanding shares of common stock or voting power*. This ownership or voting power would be the largest ownership position.),

Shares Directors' shares distribution (weight is amount of shares they should hold and number is the number of roles that should exists $\frac{role's\;value}{total\; of\;role's\;value = 10}$):
- Directors (weights: 5, number: 2)
- Mangers (weights: 3, number: 3)
- Employees (weights: 2, number: 5)

Default Setting:
The mean Series C funding in the U.S. is $72 million, so let's make it easier for calculation, let say $1 million and 10,000 shares which also make the stock price begins at $100/share


