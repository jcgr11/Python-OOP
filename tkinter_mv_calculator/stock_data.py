import yfinance as yf
import pandas as pd
import pandas.tseries.offsets as offsets

class TickerData:
    def __init__(self, ticker, date):
        self.ticker = ticker.upper()
        self.date = pd.to_datetime(date)
        self.price = self.load_data()

    def load_data(self):
        data = yf.download(self.ticker, self.date, progress=False, auto_adjust=True)
        if not data.empty:
            price = data["Close"].iloc[0]
        else:
            # Fallback to adjust the the trade date to next business day if no data was found on the specified date (e.g. weekends or holidays)
            next_trading_day = self.date + offsets.BDay(1)
            data = yf.download(self.ticker, next_trading_day, progress=False, auto_adjust=True)
            price = data["Close"].iloc[0] if not data.empty else None
        return price


    def calculate_market_value(self, shares):
        if self.price is not None:
            return shares * self.price
        else:
            return None
