import robin_stocks.robinhood as r
from Logging import login_to_robinhood

def main():
    my_stocks = login_to_robinhood()
    # for key, value in my_stocks.items():
    #     print(key, value)

    print("--------------------------------")
    for stock, value in my_stocks.items():
        print(f"Ticker: {stock}")
        for field, data in value.items():
            if field == "name":
                print(f"Name: {data}")
            if field == "average_buy_price":
                print(f"Average Buy Price: {data}")
            if field == "price":
                print(f"Price: {data}")
            if field == "quantity":
                print(f"Quantity: {data}")
            if field == "percent_change":
                print(f"Percent Change: {data}")
        totalPStock = float(value["quantity"]) * float(value["price"])
        print(f"Total Value: ${totalPStock:.2f}")
        print("--------------------------------")

    totalPortfolioValue = 0

    for stock, value in my_stocks.items():
        totalPStock = float(value["quantity"]) * float(value["price"])
        totalPortfolioValue += totalPStock
    print(f"Total Portfolio Value: ${totalPortfolioValue:.2f}")

if __name__ == "__main__":
    main()