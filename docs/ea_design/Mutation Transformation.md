# Mutation Transformation
For mutation, we have planned out 3 types of mutation: conditional, periodic, and probabilistic.

For each generation, it will run through a series of mutation and we called it a mutation transformation phrase. (order does not matter)

Users can decide which mutation will be include inside the series.

## Conditional Mutation
It is a mutation that has a 100% chance to happen for each generation if the individual satisfies the condition.

The following are a list of conditional mutation that we come up with condition (bracket indicate what properties are being affected):

- If this round's action is hold:
	- Emotional Damage (emotional resiliency)
- else (buy/sell):
	- Emotion Okay Lah (emotional resiliency)

## Emotional Damage
a mutation emphasizing towards the "decrease" of emotion resiliency

- bounded between \[0,1\] if value exceed

## Emotion Okay Lah
a mutation emphasizing towards the "increase" of emotion resiliency

- bounded between \[0,1\] if value exceed


## Periodic Mutation
It is a mutation that will occur periodically (every \#n generation)

The following are a list of periodic mutation that we come up with (bracket indicate what properties are being affected):
- get salary (wallet, emotion resiliency)
- pay for survival (wallet, emotion resiliency)
- continuous learning (ANN model)

## Get Salary
A mutation that will increase wallet amount and lower emotion resiliency ("Let's spent money!")
- A 1-to-1 negative correlation: the higher in wallet amount, the lower in emotion resiliency

$emotion \; resiliency = emotion \; resiliency \times (1 - \frac{gain}{wallet})$

## Pay for survival
A mutation that will decrease wallet amount and raise emotion resiliency ("Pay utilities, food, Insurance...etc.")
- a 1-to-1 negative correlation: the lower in wallet amount, the higher in emotion resiliency

$emotion \; resiliency = emotion \; resiliency \times (1 + \frac{loss}{wallet})$

## Continuous learning
A mutation that will modify a random neuron's weight in the ANN model based on the current best individual ("Learn from rich people!")
- clone one random weight from the individual with highest fitness value


## Probabilistic Mutation
It is the default setting of mutation where there is a probability to determine if this mutation will be performed

The following are a list of probabilistic mutation that we come up with (bracket indicate what properties are being affected):
- maybe I should change (ANN model)
- life is uncertain (wallet, emotion resiliency, ANN, shares hold)

## Maybe I should change
A mutation that will add a Norm(0, $\sigma$) value to (1 or 2 or ... or up to all weights) of an individual's ANN model

## Life is uncertain
A mutation that represent the uncertainty of events that could be happen in the real life (example: get sick, win lottery, meet a new friend and gives some advice, a gift from friends... etc)

a single point on a wheel with equal (uniform) probability for selecting wallet, emotion resiliency, ANN, shares hold to modify

- Wallet
	- Update with a Norm(0, $\sigma$) value
- emotion resiliency
	- Update with a Norm(0, $\sigma$) value ($\sigma \leqslant \frac{1}{3}$)
	- apply thresholds so that stay in boundary \[0,1\]
- ANN
	- add a single weight with a Norm(0, $sigma$) value
- Shares hold
	- random select a stock and it's fail to sell counter will be randomized between \[0,10\]
	- if the person has no shares, do nothing


