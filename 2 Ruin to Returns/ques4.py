def stationary_distribution(p, q, r, N):
    """
    Return a list of size N+1 containing the stationary distribution of the Markov chain.
    p : array of size N+1, 0 < p[i] < 1, probability of price increase
    q : array of size N+1, 0 < q[i] < 1, probability of price decrease
    r : array of size N+1, r[i] = 1 - p[i] - q[i], probability of price remaining the same
    N : int, the maximum price of the stock
    """    
    pi = [1.0] 
    for k in range(N):
        pi_next = pi[k] * (p[k] / q[k + 1])
        pi.append(pi_next)
    total = sum(pi)
    pi = [x / total for x in pi]
    return pi

def expected_wealth(p, q, r, N):
    """
    Return the expected wealth of the gambler in the long run.
    p : array of size N+1, 0 < p[i] < 1, probability of price increase
    q : array of size N+1, 0 < q[i] < 1, probability of price decrease
    r : array of size N+1, r[i] = 1 - p[i] - q[i], probability of price remaining the same
    N : int, the maximum price of the stock
    """
    pi = stationary_distribution(p, q, r, N)
    expected_value = 0
    for k in range(N + 1): 
        expected_value += k * pi[k]
    return expected_value
    
    
def expected_time(p, q, r, N, a, b):
    """
    Return the expected time for the price to reach b starting from a.
    p : array of size N+1, 0 < p[i] < 1, probability of price increase
    q : array of size N+1, 0 < q[i] < 1, probability of price decrease
    r : array of size N+1, r[i] = 1 - p[i] - q[i], probability of price remaining the same
    N : int, the maximum price of the stock
    a : int, the starting price
    b : int, the target price
    """
    if a == b: return 0.0
    pi = stationary_distribution(p,q,r,N)
    h_ab = 0
    for k in range(a, b):
        inner_sum = sum(pi[j] for j in range(k + 1))
        h_ab += (1 / (p[k] * pi[k])) * inner_sum
    return h_ab