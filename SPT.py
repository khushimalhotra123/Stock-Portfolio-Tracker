import yfinance as yf
import pandas as pd

class StockPortfolio:
    def __init__(self):
        self.portfolio = pd.DataFrame(columns=["Ticker", "Shares", "Buy Price"])
        
    def add_stock(self, ticker, shares, buy_price):
        """Adds a stock to the portfolio."""
        new_stock = pd.DataFrame({
            "Ticker": [ticker],
            "Shares": [shares],
            "Buy Price": [buy_price]
        })
        self.portfolio = pd.concat([self.portfolio, new_stock], ignore_index=True)
        print(f"Added {shares} shares of {ticker} at ${buy_price} per share.")
        
    def remove_stock(self, ticker):
        """Removes a stock from the portfolio."""
        self.portfolio = self.portfolio[self.portfolio["Ticker"] != ticker]
        print(f"Removed {ticker} from portfolio.")
        
    def get_real_time_data(self, ticker):
        """Fetches real-time stock data."""
        stock = yf.Ticker(ticker)
        data = stock.history(period="1d")
        if not data.empty:
            return data['Close'][0]
        else:
            print(f"Error: Could not fetch data for {ticker}")
            return None

    def view_portfolio(self):
        """Displays the current portfolio."""
        if self.portfolio.empty:
            print("Portfolio is empty.")
        else:
            print(self.portfolio)
        
    def track_performance(self):
        """Calculates the current value and performance of the portfolio."""
        if self.portfolio.empty:
            print("Portfolio is empty.")
            return

        self.portfolio['Current Price'] = self.portfolio['Ticker'].apply(self.get_real_time_data)
        self.portfolio['Current Value'] = self.portfolio['Shares'] * self.portfolio['Current Price']
        self.portfolio['Invested Value'] = self.portfolio['Shares'] * self.portfolio['Buy Price']
        self.portfolio['Gain/Loss (%)'] = ((self.portfolio['Current Value'] - self.portfolio['Invested Value']) / self.portfolio['Invested Value']) * 100

        print("\nPortfolio Performance:")
        print(self.portfolio[['Ticker', 'Shares', 'Buy Price', 'Current Price', 'Current Value', 'Gain/Loss (%)']])

# Example Usage:
if __name__ == "__main__":
    portfolio = StockPortfolio()

    # Adding stocks
    portfolio.add_stock("AAPL", 10, 150)
    portfolio.add_stock("TSLA", 5, 700)

    # Viewing portfolio
    portfolio.view_portfolio()

    # Tracking performance
    portfolio.track_performance()

    # Removing a stock
    portfolio.remove_stock("AAPL")
    portfolio.view_portfolio()
