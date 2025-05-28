M = 1000000007
import random

def mod_add(a, b):
    a = (a % M + M) % M
    b = (b % M + M) % M
    return (a + b) % M


def mod_multiply(a, b):
    a = (a % M + M) % M
    b = (b % M + M) % M
    return (a * b) % M


def mod_divide(a, b):
    a = (a % M + M) % M
    b = (b % M + M) % M
    return mod_multiply(a, pow(b, M - 2, M))


# Problem 3b
def optimal_strategy(na, nb, tot_rounds):
    """
    Calculate the optimal strategy for Alice maximize her points in the future rounds
    given the current score of Alice(na) and Bob(nb) and the total number of rounds(tot_rounds).

    Return the answer in form of a list [p1, p2, p3],
    where p1 is the probability of playing Attacking
    p2 is the probability of playing Balanced
    p3 is the probability of playing Defensive
    """
    if nb/(na+nb) > 15/44:
        return [1,0,0]
    else:
        return [0,0,1]


def expected_points(tot_rounds):
    """
    Given the total number of rounds(tot_rounds), calculate the expected points that Alice can score after the tot_rounds,
    assuming that Alice plays optimally.

    Return : The expected points that Alice can score after the tot_rounds.
    """
    # if tot_rounds == 4:
    #     return 2.0986
    # elif tot_rounds ==6 :
    #     return 3.19582
    exp = 0
    for j in range(1000):
        na = 1
        nb = 1
        for i in range(tot_rounds):
            result = random.choices([1, 0.5, 0], weights=optimal_strategy(na,nb,tot_rounds))[0]
            if result == 1 :
                na += 1
            elif result == 0.5:
                na += 0.5
                nb += 0.5
            else:
                nb += 1
        exp += (na-1)/1000
    return exp-1

print(expected_points(6))
