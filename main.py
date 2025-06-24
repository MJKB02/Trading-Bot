from bot.core import BasicBot
from bot.utils import setup_logger

def main():
    setup_logger()
    bot = BasicBot(testnet=True)

    print("=== Binance Futures Trading Bot ===")

    symbol = input("Enter symbol (e.g., BTCUSDT): ").upper()
    side = input("BUY or SELL: ").upper()
    order_type = input("Order Type (MARKET/LIMIT): ").upper()
    quantity = float(input("Quantity: "))

    price = None
    if order_type == "LIMIT":
        price = input("Enter limit price: ")

    order = bot.place_order(symbol, side, order_type, quantity, price)

    if order:
        print("✅ Order placed successfully!")
        print(order)
    else:
        print("❌ Order placement failed.")

if __name__ == "__main__":
    main()
