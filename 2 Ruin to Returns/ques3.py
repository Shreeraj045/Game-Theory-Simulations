def game_duration(p, q, k, t, W):
    """
    Return the expected number of rounds the gambler will play before quitting.

    p : float, 0 < p < 1, probability of winning a round
    q : float, q = 1 - p, probability of losing a round
    k : int, starting wealth
    t : int, t < k, the gambler will quit if she reaches t
    W : int, the threshold on maximum wealth the gambler can reach
    
    """
    r = q / p
    temp1 = 1 / p
    if p == q:
        temp2 =  W
    else:
        temp2 = (1 - r ** W) / (1 - r)
    temp3 = temp1 * temp2
    exp = (1 + temp3) / (r ** W)
    E = (k - t) * exp
    return E

