import yfinance as yf
import pandas as pd
import pandas.tseries.offsets as offsets


class TickerData:
    def __init__(self, ticker, start_date, end_date):
        self.ticker = ticker.upper()
        self.start_date = pd.to_datetime(start_date)
        self.end_date = pd.to_datetime(end_date)
        self.data = self.load_data()

    def adjust_date_for_weekend(self, date):
        if not date.isoweekday() in range(1, 6):
            return date - offsets.BDay(1)
        return date

    def load_data(self):
        start_date = self.adjust_date_for_weekend(self.start_date)
        end_date = self.adjust_date_for_weekend(self.end_date)
        data = yf.download(
            self.ticker, start_date, end_date, progress=False, auto_adjust=True
        )
        return data

    def calculate_bmv(self, shares):
        price = self.data.iloc[0]["Close"]
        return shares * price

    def calculate_emv(self, shares):
        price = self.data.iloc[-1]["Close"]
        return shares * price

    def calculate_holding_period_return(self):
        price = self.data["Close"]
        daily_returns = price.pct_change()
        geometric_return = (1 + daily_returns).prod() - 1
        return geometric_return
