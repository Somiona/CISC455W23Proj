# Fitness Function
We come up with **3** different fitness function:
- Asset fitness
- Zero sum fitness
- Potential growth fitness

## Asset fitness
It is considered as a multiple objective fitness function as we are trying to calculate each individual fitness by their assets which we wants to at the same time maximize the liquid asset (cash in the wallet) and the current asset (stock holds value)

The following are the formula:
$asset = \alpha(Wallet) + (1-\alpha)(\#stock\; shares \times current\;stock\;price)$
- $\alpha$ is a hyperparameter

## Zero sum fitness
It is considered a zero sum game where if one individual profits, another individual  loss. It is extended from the asset fitness from above.

The following are the formula:
$zero\;sum=\frac{asset^{(i)}_t - asset^{(i)}_{t-1}}{\frac{1}{n}\sum_{j=1} ^{n} asset^{(j)}_t}$
- $asset^{(i)}_t$ represents the i-th individual's asset at the t-th generation
- The denominator is the average of all individual's asset at the t-th generation

## Potential growth fitness
It is focusing in each individual's growth in assets and would be useful for optimization of finding *best* series of actions or weights of ANN that provide overall highest growth. It is extended from the asset fitness from above.

The following are the formula:
$growth=\frac{asset_t-asset_{t-1}}{asset_{t-1}}$
- $asset^{(i)}_t$ represents the i-th individual's asset at the t-th generation

