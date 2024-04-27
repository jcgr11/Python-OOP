import tkinter as tk


class MVAppView:
    def __init__(self, root, on_calculate):
        self.root = root
        self.setup_ui(on_calculate)

    def setup_ui(self, on_calculate):
        self.root.title("Market Value Calculator")
        tk.Label(self.root, text="Ticker:").grid(row=0, column=0)
        self.ticker_entry = tk.Entry(self.root)
        self.ticker_entry.grid(row=0, column=1)

        tk.Label(self.root, text="Purchase Date:").grid(row=1, column=0)
        self.date_entry = tk.Entry(self.root)
        self.date_entry.grid(row=1, column=1)

        tk.Label(self.root, text="Shares Purchased:").grid(row=2, column=0)
        self.shares_entry = tk.Entry(self.root)
        self.shares_entry.grid(row=2, column=1)

        self.calc_button = tk.Button(
            self.root, text="Calculate Market Value", command=on_calculate
        )
        self.calc_button.grid(row=3, column=1)
