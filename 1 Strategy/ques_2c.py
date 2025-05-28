import time
import numpy as np
import random
class Alice:
    def __init__(self):
        self.past_play_styles = [1, 1]
        self.results = [1, 0]
        self.opp_play_styles = [1, 1]
        self.points = 1

    def play_move(self):
        """
        Decide Alice's play style for the current round.
        
        Returns: 
            0 : attack
            1 : balanced
            2 : defence

        """
        lens = len(self.results)
        if self.results[-1] == 0:
            return 1
        elif self.results[-1] == 0.5:
            return 0
        else:
            if (lens - self.points) / lens > 6 / 11:
                return 0
            else:
                return 2

    def observe_result(self, own_style, opp_style, result):
        self.past_play_styles.append(own_style)
        self.results.append(result)
        self.opp_play_styles.append(opp_style)
        self.points += result
       

class Bob:
    def __init__(self):
        self.past_play_styles = [1, 1]
        self.results = [0, 1]
        self.opp_play_styles = [1, 1]
        self.points = 1

    def play_move(self):
        """
        Decide Bob's play style for the current round.

        Returns: 
            0 : attack
            1 : balanced
            2 : defence
        
        """
        if self.results[-1] == 1:
            return 2
        elif self.results[-1] == 0.5:
            return 1
        else:
            return 0
        
        
        
    
    def observe_result(self, own_style, opp_style, result):
        """
        Update Bob's knowledge after each round based on the observed results.
        
        Returns:
            None
        """
        self.past_play_styles.append(own_style)
        self.results.append(result)
        self.opp_play_styles.append(opp_style)
        self.points += result


def simulate_round(alice, bob, payoff_matrix):
    """
    Simulates a single round of the game between Alice and Bob.
    
    Returns:
        None
    """
    alice_move = alice.play_move()
    bob_move = bob.play_move()

    probabilities = payoff_matrix[alice_move][bob_move]

    result = random.choices([1, 0.5, 0], weights=probabilities)[0]

    alice.observe_result(alice_move, bob_move, result)
    bob.observe_result(bob_move, alice_move, 1 - result)

def estimate_tau(T):
    sumi = 0
    payoff_matrix = [
        [[1/2, 0, 1/2], [7/10, 0, 3/10], [5/11, 0, 6/11]],  # Alice attacks
        [[3/10, 0, 7/10], [1/3, 1/3, 1/3], [3/10, 1/2, 1/5]],  # Alice balanced
        [[6/11, 0, 5/11], [1/5, 1/2, 3/10], [1/10, 4/5, 1/10]]  # Alice defends
    ]

    num_rounds = 100000
    for i in range(num_rounds):
        j = 2
        alice = Alice()
        ap = 1
        bob = Bob()
        payoff_matrix[0][0] = [1/2,0,1/2]
        while ap < T:
            simulate_round(alice,bob,payoff_matrix)
            payoff_matrix[0][0] = [(bob.points / (alice.points + bob.points)), 0, (alice.points / (alice.points + bob.points))]
            if alice.results[-1] == 1:
                ap += 1
            j += 1
        sumi += j/num_rounds
        # print("")
    return sumi

st = time.perf_counter()
print(estimate_tau(13))
print("time -",time.perf_counter() - st)