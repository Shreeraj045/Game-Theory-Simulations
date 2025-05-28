def win_probability(p, q, k, N):
    """
    Return the probability of winning a game of chance.

    p : float, 0 < p < 1, probability of winning a round
    q : float, q = 1 - p, probability of losing a round
    k : int, starting wealth
    N : int, maximum wealth
    """
    if p == q:
        return k / N
    ratio = q / p
    win_prob = (1 - ratio ** k) / (1 - ratio ** N)
    return win_prob


def limit_win_probability(p, q, k):
    """
    Return the probability of winning when the maximum wealth is infinity.

    p : float, 0 < p < 1, probability of winning a round
    q : float, q = 1 - p, probability of losing a round
    k : int, starting wealth
    """
    if p <= q:
        return 0
    else:
        return 1 - (q / p) ** k


def game_duration(p, q, k, N):
    """
    Return the expected number of rounds to either win or get ruined.

    p : float, 0 < p < 1, probability of winning a round
    q : float, q = 1 - p, probability of losing a round
    k : int, starting wealth
    N : int, maximum wealth
    """
    r = q/p
    if p != q:
        return ((1-pow(r,k))/(1-pow(r,N))*(N/(p-q))+(k/(q-p)))
    else:
        return k*(N-k)