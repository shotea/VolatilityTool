from scipy.optimize import brentq
import math
from scipy.stats import norm

def implied_volatility(option_price, S, K, T, r):
    """Calculate implied volatility using the Black-Scholes model and Brent's method."""
    def f(sigma):
        d1 = (math.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * math.sqrt(T))
        d2 = d1 - sigma * math.sqrt(T)
        call_price = S * norm.cdf(d1) - K * math.exp(-r * T) * norm.cdf(d2)
        return call_price - option_price

    try:
        return brentq(f, 1e-5, 10)  # The volatility should be between 1e-5 and 10
    except ValueError as e:
        print(f"Error in implied_volatility: {e}")
        return None
