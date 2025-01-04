Volatility Tool
This project fetches option data, analyzes it, and calculates the implied volatility of options using the Black-Scholes model.
Table of Contents
1. Project Overview
2. File Structure
3. Setup Instructions
4. Function Explanations
5. How to Run the Project
6. Visualizing Volatility
Project Overview
The Volatility Tool is a Python-based application that fetches option data for a given ticker, analyzes expiration dates, and computes implied volatility using the Black-Scholes model. It utilizes libraries such as pandas, numpy, scipy, and yfinance for data analysis and computation.
File Structure
- main.py: Main script to fetch, process, and compute data.
- analyze_data.py: Helper functions for data analysis and implied volatility calculations.
- fetch_data.py: Fetches options data for a given ticker using yfinance.
- requirements.txt: Lists required Python libraries.
- venv/: (Optional) Virtual environment folder for project dependencies.
Setup Instructions
1. Install Python 3.7+ from the official Python website.
2. Clone the repository:
```bash
git clone https://github.com/yourusername/VolatilityTool.git
cd VolatilityTool
```
3. Create a virtual environment and activate it:
```bash
python -m venv venv
.\venv\Scripts\activate  # Windows
source venv/bin/activate  # macOS/Linux
```
4. Install dependencies:
```bash
pip install -r requirements.txt
```
Function Explanations
**black_scholes_call(S, K, T, r, sigma):**
Calculates the theoretical price of a European call option using the Black-Scholes model.
- S: Current stock price
- K: Strike price
- T: Time to expiration (in years)
- r: Risk-free interest rate
- sigma: Volatility of the underlying asset
**implied_volatility(option_price, S, K, T, r):**
Calculates the implied volatility of an option by solving for the volatility that equates the Black-Scholes price with the observed option price.
**fetch_options_data(ticker_symbol):**
Fetches options data for the given ticker using yfinance and returns call and put data for the earliest expiration date.
**plot_volatility_surface(S, strikes, expirations, r):**
Generates a 3D plot showing implied volatility across strike prices and expiration dates using matplotlib.
How to Run the Project
1. Activate the virtual environment:
```bash
.\venv\Scripts\activate  # Windows
source venv/bin/activate  # macOS/Linux
```
2. Run the main script:
```bash
python main.py
```
Visualizing Volatility
The tool includes functionality to visualize implied volatility as a surface:
1. Call the `plot_volatility_surface` function with:
- S: Current stock price
- strikes: List of strike prices
- expirations: List of times to expiration
- r: Risk-free interest rate
2. The output is a 3D plot showing how implied volatility varies with strike price and time to expiration.
