# Global variables
Here are global variables that include in the EA:
- EA general
	- Total generation
	- Current generation (The i value in for loop)
	- Population size
	- Population
- stock market
- Intraday
- A collection of every exist individual (table calendar view ish, bonus)


## Intraday
It collects every individual's action for **one** generation, then will run a function to simulate the *tradings* of that generation, a function to calculate & update this generation's closed stock price, and empty out for next generation

- Type(Intraday) = {"stock": \[\[\Individual with action value has Buy\], \[Individual with action value has Sell\],\[Success transaction\]\]}

## functions related with Intraday
Here's the list:
- collect_actions()
- trading()
- buy()



