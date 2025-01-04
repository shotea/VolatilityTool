# Volatility Tool

This project is designed to fetch option data, analyze it, and calculate the implied volatility of options using the Black-Scholes model.

## Table of Contents
- [Project Overview](#project-overview)
- [File Structure](#file-structure)
- [Setup Instructions](#setup-instructions)
- [Function Explanations](#function-explanations)
- [How to Run the Project](#how-to-run-the-project)
- [Calculating Implied Volatility](#calculating-implied-volatility)

## Project Overview

The Volatility Tool allows users to fetch option data for a given ticker, analyze the expiration dates, call options data, and compute the implied volatility using the Black-Scholes model. It is a Python-based tool that leverages the `pandas`, `numpy`, and `scipy` libraries for data analysis and computation.


## File Structure

The project follows a simple structure:

- `main.py`: This is the main file that fetches the options data, processes it, and computes the results. It is where the script is run.
- `analyze_data.py`: Contains helper functions for data analysis. This is where the Black-Scholes model and implied volatility calculations are performed.
- `requirements.txt`: Lists the required Python libraries to run the project (e.g., `pandas`, `requests`, `scipy`).
- `venv/`: The virtual environment folder that isolates your project dependencies.

## Setup Instructions

### 1. Install Python

Make sure you have Python 3.7 or higher installed. You can download it from the official website: https://www.python.org/downloads/.

### 2. Clone the Repository  

Clone the repository to your local machine:

### 3. Create and Activate a Virtual Environment
Create a virtual environment to keep the dependencies isolated:
python -m venv venv

## Activate the virtual environment:
Windows: 
.\venv\Scripts\activate

macOS/Linux:
source venv/bin/activate

### 4 Install Dependencies:
Install the necessary Python packages from requirements.txt:

pip install -r requirements.txt

This will install all the required libraries such as pandas, requests, scipy, and more.

Function Explanations
fetch_option_data(ticker)
This function retrieves the option data for a given ticker symbol from an API (e.g., Yahoo Finance or any other data provider). It returns a dataframe containing relevant options data such as strike price, last price, implied volatility, and other options details.

black_scholes_call(S, K, T, r, sigma)
This function calculates the theoretical price of a call option using the Black-Scholes formula. The parameters are:

S: Current stock price
K: Strike price of the option
T: Time to expiration (in years)
r: Risk-free interest rate
sigma: Volatility of the underlying asset
implied_volatility(option_price, S, K, T, r)
This function calculates the implied volatility of an option using the Black-Scholes model by iterating over possible volatility values. It uses scipy.optimize.brentq to find the volatility that makes the Black-Scholes call price equal to the observed option price.

get_expiry_dates(option_data)
This function extracts and returns the unique expiration dates from the fetched option data.

print_sample(option_data)
This function prints a sample of the option data, including relevant details such as the contract symbol, strike price, last price, and implied volatility.

### How to Run the Project:

## To run the project, follow these steps:

Activate the Virtual Environment: Make sure your virtual environment is activated. If it's not activated, use the following command:

.\venv\Scripts\activate   # Windows
# or
source venv/bin/activate  # macOS/Linux

Run the Main Script:

## 2 You can run the main script by using the following command:

python main.py

This will:

Fetch options data for the specified ticker.
Print the expiration dates and a sample of the options data.
Calculate and print the implied volatility for a sample option.

## Calculating Implied Volatility:

To calculate the implied volatility, the project uses the implied_volatility() function, which relies on the Black-Scholes formula.

Example:
If you have a sample option with the following details:

option_price = 90.71
S = 500.0 (current stock price)
K = 500.0 (strike price)
T = 30 / 365 (time to expiration, assuming 30 days)
r = 0.01 (risk-free interest rate, assume 1%)
You would call the implied_volatility() function like this:

iv = implied_volatility(option_price=90.71, S=500.0, K=500.0, T=30/365, r=0.01)
print(f"Implied Volatility: {iv}")

## This will output the implied volatility, such as 0.31327131576728195.

## How it Works:
1 The implied_volatility() function takes the market price of an option (option_price) and the option's other parameters (stock price, strike price, time to expiration, and risk-free rate).

2 The function iterates over possible volatility values using the brentq method from scipy.optimize to find the volatility that makes the Black-Scholes model match the observed option price.

3 The calculated implied volatility is then printed out.

Feel free to explore and modify the code to suit your needs, and contribute improvements back to the project!


### Key Points:
- **Installation Instructions**: Covers setting up the virtual environment and installing dependencies.
- **Function Details**: Breaks down each important function in the code.
- **How to Run**: Explains how to run the main script and what the output should look like.
- **Implied Volatility Calculation**: Provides an example of how implied volatility is calculated and used in the project.

This should provide a complete overview for anyone setting up and using your tool. Feel free to modify it based on any additional details you'd like to include!

```bash
git clone https://github.com/yourusername/VolatilityTool.git
cd VolatilityTool

