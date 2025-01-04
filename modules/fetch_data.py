import yfinance as yf

# Fetch options data for SPY
def fetch_options_data(ticker_symbol):
    ticker = yf.Ticker(ticker_symbol)
    expiry_dates = ticker.options
    print(f"Expiry Dates: {expiry_dates}")
    # Fetch options for the first expiry date
    options_data = ticker.option_chain(expiry_dates[0])
    return options_data.calls, options_data.puts
# modules/fetch_data.py

if __name__ == "__main__":
    calls, puts = fetch_options_data("SPY")
    print("Calls Sample:")
    print(calls.head())
