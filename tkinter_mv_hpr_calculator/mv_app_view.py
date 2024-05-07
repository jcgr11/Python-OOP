import tkinter as tk
from mv_hpr_app import mv_hpr_app


class MVAppView(mv_hpr_app):
    def __init__(self, root, on_calculate):
        super().__init__(root)
        self.setup_ui(on_calculate)

    def setup_ui(self, on_calculate):
        self.root.title("Market Value and Holding Period Return Calculator")

        tk.Label(
            self.root, 
            text="Ticker:"
            ).grid(row=0, column=0)
        
        self.ticker_entry = tk.Entry(self.root)
        self.ticker_entry.grid(row=0, column=1)

        tk.Label(
            self.root, 
            text="Start Date:"
            ).grid(row=1, column=0)
        
        self.start_date_entry = tk.Entry(self.root)
        self.start_date_entry.grid(row=1, column=1)

        tk.Label(
            self.root, 
            text="End Date:"
            ).grid(row=2, column=0)
        
        self.end_date_entry = tk.Entry(self.root)
        self.end_date_entry.grid(row=2, column=1)

        tk.Label(
            self.root, 
            text="Shares Purchased:"
            ).grid(row=3, column=0)
        
        self.shares_entry = tk.Entry(self.root)
        self.shares_entry.grid(row=3, column=1)

        self.calc_button = tk.Button(
            self.root, 
            text="Calculate", 
            command=on_calculate)
        
        self.calc_button.grid(row=4, column=1)

        self.results_text = tk.Text(
            self.root, 
            height=5, width=70)
        
        self.results_text.grid(row=5, column=0, columnspan=2)
