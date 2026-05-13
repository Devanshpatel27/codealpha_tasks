stock_price = {
        "CODE ALPHA": 1000,
        "APPLE": 500,
        "TESLA": 250,
        "NVIDIA": 500,
        "META": 400,
        "NETFLIX": 350,
        "MICROSOFT": 550
}
total_investment = 0

print("Available Stocks: ")

for stock in stock_price:
    print(stock, ":", stock_price[stock])   

stock_name = input("\nEnter stock name: ").upper()
quantity = int(input("Enter quantity: "))   

if stock_name in stock_price:
    price = stock_price[stock_name]
    investment = price * quantity
    total_investment += investment

    print("\nStock:", stock_name)
    print("Price:", price)
    print("Quantity:", quantity)
    print("Total Investment:", investment)

    with open("portfolio.txt", "w") as file:
        file.write(f"Stock: {stock_name}\n")
        file.write(f"Price: {price}\n")
        file.write(f"Quantity: {quantity}\n")
        file.write(f"Total Investment: {investment}\n")

    print("\nData saved in portfolio.txt")
else:
    print("Stock not found!")
