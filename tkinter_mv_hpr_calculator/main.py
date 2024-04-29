import tkinter as tk
from mv_app_controller import MarketValueAppController

def main():
    root = tk.Tk()
    app = MarketValueAppController(root)
    root.mainloop()

if __name__ == "__main__":
    main()
