# Probabilistic Modeling and Game Strategy Analysis

This repository contains implementations of various probabilistic models and game strategies. The project is split into two main components: "Ruin to Returns" and "Strategy".

## Ruin to Returns

This component focuses on gambling models, Markov chains, and stock price analysis using probabilistic methods.

### Implementations:

1. **Classic Gambler's Ruin Problem** (`ques1.py`)
   - Calculates the probability of a gambler winning a game of chance
   - Finds the probability when maximum wealth approaches infinity
   - Computes the expected duration of the game until either winning or getting ruined

2. **Aggressive Gambling Strategy** (`ques2.py`)
   - Implements a recursive dynamic programming approach for an aggressive gambling strategy
   - Calculates win probability and expected game duration with this strategy

3. **Quitting Strategy** (`ques3.py`)
   - Models a gambler who quits if wealth drops to a certain threshold
   - Calculates the expected number of rounds before quitting

4. **Stock Price Analysis** (`ques4.py`)
   - Computes the stationary distribution of a Markov chain representing stock prices
   - Calculates expected wealth in the long run based on price movements
   - Determines the expected time for a stock price to reach a target value from a starting point

## Strategy

This component focuses on game theory, optimal strategies, and simulation of competitive gameplay.

### Implementations:

1. **Probability and Expected Value Calculations** (`ques_1.py`)
   - Implements modular arithmetic operations for probability calculations
   - Computes probability, expectation, and variance for specific game scenarios

2. **Rock-Paper-Scissors Style Game** (`ques_2a.py`, `ques_2b.py`, `ques_2c.py`)
   - Simulates a strategic game between two players (Alice and Bob)
   - Players can choose different play styles (Attack, Balanced, Defense)
   - Implements decision-making strategies based on previous game outcomes
   - Simulates rounds with payoff matrices determining win probabilities

3. **Optimal Strategy Determination** (`ques_3b.py`)
   - Calculates optimal strategies to maximize points in competitive scenarios
   - Uses probability thresholds to determine the best action
   - Computes expected points for different numbers of rounds

## Mathematical Foundation

The implementations rely on various concepts from:
- Probability theory
- Markov chains
- Dynamic programming
- Game theory
- Expected value calculations

## Usage

Each Python file contains specific functions that can be imported and used independently. The functions are well-documented with docstrings explaining the parameters and return values.

Example:
```python
from ruin_to_returns.ques1 import win_probability

# Calculate probability of winning with:
# p=0.4 (win probability per round)
# q=0.6 (loss probability per round)
# k=10 (starting wealth)
# N=100 (maximum wealth)
prob = win_probability(0.4, 0.6, 10, 100)
print(f"Probability of winning: {prob}")
```
