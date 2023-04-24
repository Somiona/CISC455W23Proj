# CISC455W23Proj
> [!ATTENTION|style:flat]
> **EMOTIONAL DAMAGE! Haiya**

## [NEW! View document at github pages](https://somiona.github.io/CISC455W23Proj/)

## What is this project about?
we are trying to create a stock market **simulation** using Evolutionary Algorithm (EA).

### Background

### What are we interested in?
- We are interested in creating a stochastic stock market trends based on number of investors.
- Why is stock markets unpredictable?

### Questions we want to answer throughout this project
- On average, at what population size the stock price become unpredictable?
- On average, what series of actions or behaviour for an investor is considered successful?

## How to run the project
> [!WARNING|style:flat]
> Use `CISC455W23Proj.code-workspace` instead of directly open the folder.

```terminal
#|info| If you are using unix-like system
$| chmod +x launch_all.sh
$| .\launch_all.sh
#|info| If you are using windows, launch your powershell
>| Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
>| ./launch_all.ps1
```

Before running `launch_all.sh`, make sure you've run `pipenv install` inside the root dir of this project!
Not inside Backend