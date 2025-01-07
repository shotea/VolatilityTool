import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
from scipy.optimize import brentq
from datetime import datetime, timedelta

# Black-Scholes formula
def black_scholes_call(S, K, T, r, sigma):
    """
    Calculate the Black-Scholes option price for a call option.
    
    S : float : Current stock price
    K : float : Strike price
    T : float : Time to expiration in years
    r : float : Risk-free interest rate (annual)
    sigma : float : Volatility of the stock (annual)
    
    Returns the option price.
    """
    d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    
    call_price = S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
    return call_price

# Implied volatility function using Brent's method
def implied_volatility(S, K, T, r, market_price):
    """
    Calculate the implied volatility using the Brent's method.
    
    S : float : Current stock price
    K : float : Strike price
    T : float : Time to expiration in years
    r : float : Risk-free interest rate (annual)
    market_price : float : Market price of the option
    
    Returns the implied volatility.
    """
    def objective_function(sigma):
        return black_scholes_call(S, K, T, r, sigma) - market_price

    return brentq(objective_function, 1e-6, 5)

# 3D plotting of option prices vs. strike price and time to expiration
def plot_3d_surface(S, r, market_price, expiry_dates, strikes):
    """
    Plot a 3D surface for implied volatility.
    
    S : float : Current stock price
    r : float : Risk-free interest rate
    market_price : float : Market price of the option
    expiry_dates : list : Available expiry dates
    strikes : list : List of strike prices
    """
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    
    X, Y = np.meshgrid(strikes, range(len(expiry_dates)))
    Z = np.zeros(X.shape)
    
    # Store the calculated implied volatilities for printing
    implied_vols = []
    
    for i, expiry in enumerate(expiry_dates):
        # Calculate time to expiration
        T = (np.datetime64(expiry) - np.datetime64('today')).astype('timedelta64[D]').item().days / 365
        for j, strike in enumerate(strikes):
            try:
                sigma = implied_volatility(S, strike, T, r, market_price)
                Z[i, j] = sigma
                implied_vols.append((expiry, strike, sigma))
            except ValueError:
                Z[i, j] = np.nan  # If no solution, set NaN to avoid plot issues
    
    # Plot the 3D surface
    ax.plot_surface(X, Y, Z, cmap='viridis', edgecolor='none')
    ax.set_xlabel('Strike Price')
    ax.set_ylabel('Expiration Date')
    ax.set_zlabel('Implied Volatility')
    ax.set_title('Implied Volatility Surface')
    
    # Set expiration dates as labels on the y-axis
    ax.set_yticks(range(len(expiry_dates)))
    ax.set_yticklabels(expiry_dates)
    
    # Add annotations for implied volatility values (only for a few points for clarity)
    for i, expiry in enumerate(expiry_dates):
        for j, strike in enumerate(strikes):
            if not np.isnan(Z[i, j]):
                ax.text(X[i, j], Y[i, j], Z[i, j], f'{Z[i, j]:.2f}', color='black', fontsize=8)

    plt.show()
    
    # Print implied volatility calculations
    print("\nImplied Volatility Calculations:")
    for expiry, strike, sigma in implied_vols:
        print(f"Expiration: {expiry}, Strike: {strike}, Implied Volatility: {sigma:.4f}")

def get_available_expiration_dates(ticker):
    """
    Fetch available expiration dates for a given ticker using Yahoo Finance.
    
    ticker : str : Stock symbol
    
    Returns a list of expiration dates.
    """
    try:
        # Fetch options data for the ticker
        stock = yf.Ticker(ticker)
        options_dates = stock.options
        
        # Return the list of available expiration dates
        return options_dates
    except Exception as e:
        print(f"Error fetching expiration dates: {e}")
        return []

def main():
    ticker = input("Enter the ticker symbol (e.g., SPY, AAPL, TSLA): ").upper()
    S = float(input(f"Current Stock Price for {ticker}: "))
    
    # Get the available expiration dates dynamically
    expiry_dates = get_available_expiration_dates(ticker)
    
    if not expiry_dates:
        print("No expiration dates found, exiting.")
        return
    
    print("\nAvailable Expiration Dates:")
    for i, expiry in enumerate(expiry_dates):
        print(f"{i + 1}. {expiry}")
    
    # User selects the expiration date
    try:
        selected_expiry_idx = int(input(f"Select the expiration date (1-{len(expiry_dates)}): ")) - 1
        if selected_expiry_idx < 0 or selected_expiry_idx >= len(expiry_dates):
            print("Invalid selection, exiting.")
            return
    except ValueError:
        print("Invalid input, please enter a number.")
        return

    selected_expiry = expiry_dates[selected_expiry_idx]
    
    # Get user input for option data
    market_price = float(input("Enter the market price of the option: "))
    strike_price = float(input("Enter the strike price: "))
    r = float(input("Enter the risk-free interest rate (e.g., 0.05 for 5%): "))
    
    # Strikes (range of strike prices to choose from)
    strikes = np.arange(75, 500, 5)
    
    # Plot the implied volatility surface
    plot_3d_surface(S, r, market_price, expiry_dates, strikes)

if __name__ == "__main__":
    main()
