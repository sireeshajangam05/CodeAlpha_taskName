# Stock Portfolio Tracker

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "MSFT": 310,
    "GOOGL": 140
}

portfolio = {}
total_investment = 0

while True:
    stock = input("Enter stock symbol (AAPL, TSLA, MSFT, GOOGL) or 'done' to finish: ").upper()
    if stock == "DONE":
        break
    if stock not in stock_prices:
        print("❌ Stock not found in price list.")
        continue
    
    qty = int(input(f"Enter quantity of {stock}: "))
    portfolio[stock] = portfolio.get(stock, 0) + qty

# Calculate total investment
print("\n--- Portfolio Summary ---")
for stock, qty in portfolio.items():
    investment = stock_prices[stock] * qty
    total_investment += investment
    print(f"{stock}: {qty} shares → ${investment}")

print(f"\n💰 Total Investment Value: ${total_investment}")

# Optional: Save to file
save = input("Do you want to save results to a file? (y/n): ").lower()
if save == "y":
    with open("portfolio.txt", "w") as f:
        for stock, qty in portfolio.items():
            f.write(f"{stock}: {qty} shares → ${stock_prices[stock] * qty}\n")
        f.write(f"\nTotal Investment Value: ${total_investment}\n")
    print("✅ Portfolio saved to portfolio.txt")