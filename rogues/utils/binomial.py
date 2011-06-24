from math import factorial

def binomial(n, k):
    """binomial(n, k): return the binomial coefficient (n k)."""

    if k < 0 or k > n:
        return 0
    if k == 0 or k == n:
        return 1
    return factorial(n) // (factorial(k) * factorial(n-k))