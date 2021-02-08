import requests

from plotly import graph_objects
from datetime import datetime

COINBASE_API_CANDELSTICKS_URL = \
    'https://api.pro.coinbase.com/products/{}/candles?granularity={}'



def main():
    resp = requests.get(
        COINBASE_API_CANDELSTICKS_URL.format(
        'BTC-USD',
        '86400'
        )
    )

resp_json = resp.json()

dates = []
lows = []
highs = []
opens = []
closes = []

for candlestick_data in resp_json:
    dates.append(datetime.fromtimestamp(candlestick_data[0]))
    lows.append(candlestick_data[1])
    highs.append(candlestick_data[2])
    opens.append(candlestick_data[3])
    closes.append(candlestick_data[4])

figure = graph_objects.Figure(
    data =[
        graph_objects.Candlestick(
            x =dates,
            open = opens,
            high = highs,
            low = lows,
            close = closes,
        )
    ],
    layout = graph_objects.Layout(title={
        "text": "BTC/USD Daily Chart"
    })
)
figure.show()
if __name__ == '__main__':
    main()
