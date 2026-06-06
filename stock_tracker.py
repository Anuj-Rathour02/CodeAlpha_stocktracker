# Stock Portfolio Tracker

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 330,
    "AMZN": 150
}

portfolio = {}
total_value = 0

print("=" * 40)
print("      STOCK PORTFOLIO TRACKER")
print("=" * 40)

while True:
    stock = input("\nEnter stock symbol (or 'done' to finish): ").upper()

    if stock == "DONE":
        break

    if stock not in stock_prices:
        print("Invalid stock symbol! Please try again.")
        continue

    try:
        quantity = int(input(f"Enter quantity of {stock}: "))

        if quantity <= 0:
            print("Quantity must be greater than 0.")
            continue

        if stock in portfolio:
            portfolio[stock] += quantity
        else:
            portfolio[stock] = quantity

        print(f"{stock} added successfully!")

    except ValueError:
        print("Please enter a valid number.")

# Display Portfolio Summary
print("\n" + "=" * 40)
print("         PORTFOLIO SUMMARY")
print("=" * 40)

if len(portfolio) == 0:
    print("No stocks added.")
else:
    for stock, quantity in portfolio.items():
        price = stock_prices[stock]
        investment = price * quantity
        total_value += investment

        print(
            f"{stock:<8} Qty: {quantity:<5} "
            f"Price: ${price:<5} "
            f"Value: ${investment}"
        )

    print("-" * 40)
    print(f"Total Portfolio Value: ${total_value}")

    # Save to file
    with open("portfolio_report.txt", "w") as file:
        file.write("STOCK PORTFOLIO REPORT\n")
        file.write("=" * 30 + "\n")

        for stock, quantity in portfolio.items():
            price = stock_prices[stock]
            investment = price * quantity

            file.write(
                f"{stock} | Qty: {quantity} | "
                f"Price: ${price} | Value: ${investment}\n"
            )

        file.write("\n")
        file.write(f"Total Portfolio Value: ${total_value}")

    print("\nPortfolio report saved as 'portfolio_report.txt'")