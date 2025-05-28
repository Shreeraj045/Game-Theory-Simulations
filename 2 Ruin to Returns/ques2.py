def win_probability(p, q, k, N,dp = None):
    """
    Return the probability of winning while gambling aggressively.
    
    p : float, 0 < p < 1, probability of winning a round
    q : float, q = 1 - p, probability of losing a round
    k : int, starting wealth
    N : int, maximum wealth
    """
    if dp is None:
        dp = {}
    if k == 0:
        return 0 
    if k >= N:
        return 1  
    if k in dp:
        return dp[k]
    if k < N / 2:
        dp[k] = p * win_probability(p, q, 2 * k, N, dp)
    else:
        dp[k] = p + q * win_probability(p, q, 2 * k - N, N, dp)
    return dp[k]

def game_duration(p, q, k, N,dp=None):
    """
    Return the expected number of rounds to either win or get ruined while gambling aggressively.
    
    p : float, 0 < p < 1, probability of winning a round
    q : float, q = 1 - p, probability of losing a round
    k : int, starting wealth
    N : int, maximum wealth
    """
    if dp is None:
        dp = {}
    if k == 0 or k==N:
        return 0   
    if k == N/2:
        return 1
    if k in dp:
        return dp[k]
    if k < N / 2:
        dp[k] = 1  + p * game_duration(p, q, 2 * k, N, dp)
    else:
        dp[k] = 1  + q * game_duration(p, q, 2 * k - N, N, dp)
    return dp[k]
