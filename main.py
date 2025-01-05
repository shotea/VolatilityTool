import yfinance as yf
from modules.analyze_data import implied_volatility
from datetime import datetime

# Fetch options data for a given ticker symbol and expiration date
def fetch_options_data(ticker_symbol, expiry_date=None):
    ticker = yf.Ticker(ticker_symbol)
    expiry_dates = ticker.options
    print(f"Available Expiry Dates: {expiry_dates}")

    # Let the user select an expiration date
    if not expiry_date:
        print("Select an expiration date from the list above:")
        expiry_date = input("Enter the expiration date (e.g., 2025-01-10): ")
        if expiry_date not in expiry_dates:
            print("Invalid expiration date. Please restart and select a valid date.")
            return None, None

    options_data = ticker.option_chain(expiry_date)
    return options_data.calls, options_data.puts

def get_current_stock_price(ticker_symbol):
    """Fetch the current stock price for a given ticker."""
    ticker = yf.Ticker(ticker_symbol)
    return ticker.history(period="1d")["Close"].iloc[0]

def main():
    # Input ticker symbol and fetch current stock price
    ticker = input("Enter the ticker symbol (e.g., SPY, AAPL, TSLA): ").upper()
    stock_price = get_current_stock_price(ticker)
    print(f"Current Stock Price for {ticker}: {stock_price:.2f}")

    # Fetch options data and allow user to select expiration date
    calls, puts = fetch_options_data(ticker)

    # Check if calls and puts data were fetched successfully
    if calls is None or puts is None:
        return

    print("Calls Sample:")
    print(calls.head())

    # Input parameters for implied volatility calculation
    try:
        option_price = float(input("Enter the market price of the option: "))
        K = float(input("Enter the strike price: "))
        r = float(input("Enter the risk-free interest rate (e.g., 0.05 for 5%): "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return

    # Calculate the time to expiration based on today's date and selected expiration date
    try:
        expiration_date = datetime.strptime('2025-01-10', '%Y-%m-%d')  # Use the user-selected expiration date
        today = datetime.now()
        if expiration_date < today:
            print("The selected expiration date is in the past. Please select a future expiration date.")
            return
        T = (expiration_date - today).days / 365.0  # Convert days to years
        print(f"Time to expiration: {T:.3f} years")
    except Exception as e:
        print(f"Error calculating time to expiration: {e}")
        return

    # Calculate implied volatility
    try:
        implied_vol = implied_volatility(option_price, stock_price, K, T, r)
        print(f"Implied Volatility: {implied_vol:.2%}")
    except ValueError as e:
        print(f"Error calculating implied volatility: {e}")
        print("This might be due to unrealistic input parameters or market conditions.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
