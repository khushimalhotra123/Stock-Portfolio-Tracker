Stock Portfolio Tracker 📈

A Python-based Stock Portfolio Tracker that helps users track their stock investments in real-time. This tool allows you to add, remove, and monitor the performance of various stocks using live market data from financial APIs such as Yahoo Finance (via yfinance).

Table of Contents

* Features
* How It Works
* Installation
* Usage
* Future Enhancements
* Contributing
* License
  
Features

* Add/Remove Stocks: Easily add new stocks to your portfolio or remove existing ones.
* Real-Time Data: Fetches real-time stock prices using the yfinance library.
* Performance Tracking: Calculates current value, total investment, and profit/loss for each stock.
* Portfolio Overview: View all stocks in your portfolio along with relevant financial details such as buy price, current price, and gain/loss percentage.
* Dynamic Updates: Update your portfolio with the latest stock prices at any time.
  
How It Works

* Stock Data: The application uses the Yahoo Finance API (via yfinance) to fetch real-time stock prices.
* Portfolio Management: Users can manage their stock portfolio by adding and removing stocks, specifying the number of shares, and the price they purchased at.
* Performance Metrics: It calculates key metrics such as the total invested value, current market value, and profit/loss percentage for each stock in the portfolio.
Installation

1. Clone the repository: git clone https://github.com/your-username/stock-portfolio-tracker.git
2. cd stock-portfolio-tracker 
3. Install required dependencies: You need to install the required libraries before running the application. This project uses Python 3.x and the following libraries:
    * yfinance
    * pandas
4. Install them using pip: pip install yfinance pandas 
5. Ensure Python is installed: Make sure you are using Python 3.x. You can check by running: python --version 
Usage

1. Run the script: Once the dependencies are installed, run the stock_portfolio_tracker.py script: python stock_portfolio_tracker.py 
2. Adding a Stock: When prompted, you can add a stock to your portfolio by providing:
    * Ticker symbol (e.g., AAPL for Apple).
    * Number of shares.
    * The price at which you bought the stock.
3. Viewing and Updating Portfolio:
    * View the current state of your portfolio, including real-time updates on current stock prices and profit/loss.
    * Update the portfolio at any time to fetch the latest stock data and recalculate the performance metrics.
4. Removing a Stock: You can remove any stock from the portfolio by providing its ticker symbol.
Example

Here’s a simple example of how the portfolio tracker works:
# Adding stocks
tracker.add_stock("AAPL", 10, 150)  # Adds 10 shares of AAPL bought at $150
tracker.add_stock("TSLA", 5, 700)   # Adds 5 shares of TSLA bought at $700

# Viewing the portfolio
tracker.view_portfolio()

# Updating the portfolio with real-time stock prices
tracker.update_portfolio()

# Removing a stock
tracker.remove_stock("AAPL")

Future Enhancements

Some ideas for future development:
* Multiple Portfolios: Support for tracking multiple portfolios.
* Historical Data: Track and visualize the historical performance of the portfolio over time.
* Export Reports: Add functionality to export portfolio performance to CSV or Excel.
* API Integration: Integrate with more financial data providers like Alpha Vantage or IEX Cloud for better accuracy.
* User Authentication: Allow users to save and load their portfolio for future sessions.
Contributing

Contributions are welcome! If you’d like to contribute:
1. Fork the repository.
2. Create a feature branch (git checkout -b feature-branch).
3. Make your changes.
4. Commit your changes (git commit -m 'Added some feature').
5. Push to the branch (git push origin feature-branch).
6. Open a pull request.
License

This project is licensed under the MIT License - see the LICENSE file for details.
