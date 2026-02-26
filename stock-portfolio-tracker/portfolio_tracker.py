stock_prices={
    "APPL": 180,
    "GOOG": 200,
    "MSFT": 170,
    "AMZN": 140,
    "TSLA": 250,
    }
total_investment=0
portfolio=[]
print(" Welcome to stock portfolio tracker")
print("--------------------------------")
while True:
    stock_name=input("Enter stock name(or 'Q' to quit):").upper()
    if stock_name=="Q":
        break
    if stock_name not in stock_prices:
        print("stock not available!")
        continue
    quantity=int(input("Enter quantity:"))
    price=stock_prices[stock_name]
    investment=price*quantity
    total_investment+=investment
    new_stock_entery= (stock_name, quantity, investment)
    portfolio.append(new_stock_entery)
    print(f"{stock_name} added / Value: ${investment}\n")
    print("\nSummery of this sesstion")
    print("--------------------------")
    print(f"stock: {stock_name}")
    print(f"qunatity: {quantity}")
    print(f"Value: ${investment}")
    print(f"Total investment Value: ${total_investment}")

    save=input("Do you want to save this to file(Yes/No)").lower()
    if save=="yes":
        with open("portfolio.txt","a")as file:
          file.write("portfolio Report\n")
          file.write("-------------------\n")
          file.write(f"stock: {stock_name}\n")
          file.write(f"quantity: {quantity}\n")
          file.write(f"Value: ${investment}\n")
          file.write(f"total investment:{total_investment}")
          file.write("-------------------------------\n")
        print(f"{stock_name} save to portfolio.txt")
print("Thank you for using Stock Portfolio tracker")