from modules import analyze_data
import matplotlib.pyplot as plt
import numpy as np

def plot_volatility_surface(S, strikes, expirations, r):
    """Generate and plot a volatility surface."""
    from modules.analyze_data import implied_volatility
    volatility_surface = np.array([
        [implied_volatility(5, S, K, T, r) for K in strikes]
        for T in expirations
    ])
    X, Y = np.meshgrid(strikes, expirations)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, volatility_surface, cmap='viridis')
    ax.set_xlabel("Strike Price")
    ax.set_ylabel("Time to Expiration")
    ax.set_zlabel("Implied Volatility")
    plt.show()
