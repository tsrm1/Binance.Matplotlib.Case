from binance import Client
# from binance import AsyncClient
import matplotlib.pyplot as plt


binance_client = Client()

# количество монет в портфеле
btc_value = 0.01
eth_value = 2
ltc_value = 10

# получаем текущий курс обмена указанной монеты
def get_ticker_price(symbol: str):
    ticker_data = binance_client.get_ticker(symbol=symbol)
    return float(ticker_data['lastPrice'])

btc_exchange_rate = get_ticker_price('BTCUSDT')
eth_exchange_rate = get_ticker_price('ETHUSDT')
ltc_exchange_rate = get_ticker_price('LTCUSDT')

btc_usd_amount = btc_value * btc_exchange_rate
eth_usd_amount = eth_value * eth_exchange_rate
ltc_usd_amount = ltc_value * ltc_exchange_rate
print(btc_usd_amount, eth_usd_amount, ltc_usd_amount)

total_value = btc_usd_amount + eth_usd_amount + ltc_usd_amount
print("Total value: ", total_value)


plt.pie([btc_usd_amount, eth_usd_amount, ltc_usd_amount],
        labels=[
            f"BTC: {round(btc_usd_amount, 2)}",
            f"ETH: {round(eth_usd_amount, 2)}",
            f"LTC: {round(ltc_usd_amount, 2)}"
        ])
plt.legend(title=f"Total value: {round(total_value, 2)}")
plt.show()


