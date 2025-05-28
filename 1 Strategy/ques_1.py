M=1000000007

def mod_add(a, b):
    a=(a%M+M)%M
    b=(b%M+M)%M
    return (a+b)%M
def mod_multiply(a, b):
    a=(a%M+M)%M
    b=(b%M+M)%M
    return (a*b)%M
def mod_divide(a, b):
    a=(a%M+M)%M
    b=(b%M+M)%M
    return mod_multiply(a, pow(b, M-2, M))
memo = {}
def calc_prob(alice_wins, bob_wins):
    if (alice_wins, bob_wins) in memo:
        return memo[(alice_wins, bob_wins)]

    if alice_wins == 1 and bob_wins == 1:
        return 1
    p = 0
    total_wins = alice_wins + bob_wins - 1

    if alice_wins > 1:
        alice_prob = mod_divide(bob_wins, total_wins)
        p = mod_add(p, mod_multiply(alice_prob, calc_prob(alice_wins - 1, bob_wins)))

    if bob_wins > 1:
        bob_prob = mod_divide(alice_wins, total_wins)
        p = mod_add(p, mod_multiply(bob_prob, calc_prob(alice_wins, bob_wins - 1)))

    memo[(alice_wins, bob_wins)] = p
    return p


def calc_expectation(t):
    expectation = 0
    for x in range(1,t + 1):
        p_xy = calc_prob(x,t-x)
        expectation = mod_add(expectation, mod_multiply(2*x-t, p_xy))

    return expectation

def calc_variance(t):
    variance = 0
    for x in range(1,t+1):
        p_xy = calc_prob(x,t-x)
        variance = mod_add(variance,mod_multiply((2*x-t)**2,p_xy))
    return variance


print(calc_prob(99,48))
print(calc_expectation(48))
print(calc_variance(5))