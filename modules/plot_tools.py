import matplotlib.pyplot as plt
import numpy as np
from modules.analyze_data import implied_volatility

def plot_volatility_surface(S, strikes, expirations, r):
    """Plot the implied volatility surface."""
    volatilities = []
    
    # Loop through each strike and expiration to compute implied volatilities
    for K in strikes:
        implied_vols = []
        for T in expirations:
            vol = implied_volatility(5, S, K, T, r)  # Example for option price (5), could adjust
            if vol is not None:
                implied_vols.append(vol)
            else:
                implied_vols.append(np.nan)
        volatilities.append(implied_vols)

    # Plotting
    volatilities = np.array(volatilities)
    X, Y = np.meshgrid(strikes, expirations)
    fig = plt.figure(figsize=(10, 7))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, volatilities, cmap='viridis')

    ax.set_xlabel('Strike Price')
    ax.set_ylabel('Time to Expiration (Years)')
    ax.set_zlabel('Implied Volatility')
    ax.set_title('Implied Volatility Surface')

    plt.show()
