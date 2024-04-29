from tkinter import messagebox
import tkinter as tk
from mv_app_view import MVAppView
from stock_data import TickerData
from mv_hpr_app import mv_hpr_app

class MarketValueAppController(mv_hpr_app):
    def __init__(self, root):
        super().__init__(root)
        self.view = MVAppView(root, self.calculate)

    def calculate(self):
        ticker = self.view.ticker_entry.get().upper()
        start_date = self.view.start_date_entry.get()
        end_date = self.view.end_date_entry.get()
        shares_str = self.view.shares_entry.get()

        try:
            shares = int(shares_str)
            finance_data = TickerData(ticker, start_date, end_date)
            bmv = finance_data.calculate_bmv(shares)
            emv = finance_data.calculate_emv(shares)
            holding_period_return = finance_data.calculate_holding_period_return()

            if bmv is None or emv is None:
                messagebox.showerror(
                    "Data Error",
                    "Market value could not be calculated for one or both dates. Check your dates and try again.",
                )
                return

            if holding_period_return is None:
                messagebox.showerror(
                    "Data Error",
                    "Holding period return could not be calculated. Check your dates and try again.",
                )
                return

            result = f"Beginning Market Value: ${round(bmv, 2)}\nEnding Market Value: ${round(emv, 2)}\nHolding Period Return: {round(holding_period_return * 100, 2)}%"
            self.view.results_text.delete("1.0", tk.END)
            self.view.results_text.insert(tk.END, result)
        except ValueError:
            messagebox.showerror(
                "Invalid Input", "Please ensure all inputs are correct and numeric."
            )
