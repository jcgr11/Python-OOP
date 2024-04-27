from tkinter import messagebox
from mv_app_view import MVAppView
from stock_data import TickerData


class MarketValueAppController:
    def __init__(self, root):
        self.view = MVAppView(root, self.calculate)

    def calculate(self):
        ticker = self.view.ticker_entry.get().upper()
        date = self.view.date_entry.get()
        shares_str = self.view.shares_entry.get()

        try:
            shares = int(shares_str)
            finance_data = TickerData(ticker, date)
            market_value = finance_data.calculate_market_value(shares)
            if market_value is not None:
                messagebox.showinfo(
                    "Market Value", f"The Market Value of your stock purchase is ${market_value:.2f}"
                )
            else:
                messagebox.showerror(
                    "Data Error", "Could not retrieve stock price for the given date."
                )
        except ValueError:
            messagebox.showerror(
                "Invalid Input",
                "Please ensure all inputs are correct.",
            )
