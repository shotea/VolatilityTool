import numpy as np
from scipy.stats import norm
from scipy.optimize import brentq

def black_scholes_call(S, K, T, r, sigma):
    """Calculate the call option price using Black-Scholes formula."""
    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    return S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)

def implied_volatility(option_price, S, K, T, r):
    """Calculate implied volatility."""
    def f(sigma):
        return black_scholes_call(S, K, T, r, sigma) - option_price
    return brentq(f, 1e-5, 10)
