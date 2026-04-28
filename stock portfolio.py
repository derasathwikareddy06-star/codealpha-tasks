# Task 2: Stock Portfolio Tracker

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140,
    "AMZN": 160,
    "MSFT": 300
}

total_investment = 0

print("Available Stocks:", stock_prices)

# User input
stock_name = input("Enter stock name: ").upper()
quantity = int(input("Enter quantity: "))

# Check stock exists
if stock_name in stock_prices:
    total_investment = stock_prices[stock_name] * quantity
    print("Total Investment Value: $", total_investment)

    # Optional file saving
    file = open("portfolio.txt", "w")
    file.write(f"Stock: {stock_name}\nQuantity: {quantity}\nTotal Value: ${total_investment}")
    file.close()

    print("Portfolio saved in portfolio.txt")

else:
    print("Stock not found!")