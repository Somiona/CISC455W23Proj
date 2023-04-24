# Recombination Transformation
For recombination, we have planned out 3 types of recombination: absolute recombination, periodic recombination, and probabilistic recombination.

For each generation, it will run through a series of recombination functions and we called it a recombination transformation phrase.

Users can decide which recombination will be include inside the series.

Also, for recombination functions, there should be 3 levels: crossover, group recombination (2-10 individuals, less than 10% of population), societal recombination (10%-100% of population)

## Absolute Recombination
It is a recombination that has a 100% chance to happen for each generation.

The following are a list of absolute recombination that we come up with (inside bracket indicate the level and what properties are being affected):
- teach me something bro (crossover: wallet, ANN)
- new investors (group: wallet, ANN)

## Teach me something bro
It is a crossover that "balance" $\alpha\%$ of the entire ANN of two individuals and the the "fitter" individual will receive a $\beta\%$ of wallet from the other individual.
- idea comes from a Chinese proverb "近朱者赤，近墨者黑" (One takes the behaviour of one's company.)
- $\alpha \in [0,1], \; \beta \in [0,0.5]$

1. Compare and decide which individual is less fitter
the less fitter (learner) will learn from the better individual
2. learn distance = $fitter's \; ANN - learner's \; ANN$
3. learner's ANN += $\alpha \times learn\;distance$
4. fitter's ANN += $\frac{(1-\alpha)}{2} \times (-learn\;distance)$
5. thank you money = learner $\times \beta$
6. learner's wallet -= thank you money
7. fitter's wallet += thank you money

## new investors
It is a conditional group recombination, it happens when some individual(s) reach their death age and the simulation need to introduce new investor(s) to maintain the fixed size of population.


## Periodic Recombination
It is a recombination that will occur periodically (every \#n generation)

The following are a list of periodic recombination that we come up with (inside bracket indicate the level and what properties are being affected):
- attend lecture (group: wallet, ANN)
- money give it to you (crossover, group, societal: wallet)


## Probabilistic Recombination
There is a probability to determine if this recombination will be performed

The following are a list of  that we come up with (inside bracket indicate the level and what properties are being affected):
- big news (societal: emotion resiliency, wallet, ANN)


