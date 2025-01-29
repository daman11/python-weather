import tkinter as tk
from tkinter import filedialog, ttk
import pandas as pd
from openpyxl.styles.fills import fills


def load_excel_file():
    file_path = filedialog.askopenfilename(
        title="Wybierz plik Excel",
        filetypes=[('Excel Files', '*.xlsx')]
    )
    if file_path:
        df = pd.read_excel(file_path)
        display_data(df)

def display_data(df):
    columns = list(df.columns)
    table_cols = ttk.Treeview(columns=columns, show="headings", height=20)
    table_cols.pack(fill="both", expand=True)

    for col in columns:
        table_cols.heading(col, text=col)
        table_cols.column(col, width=100)

    for index, row in df.iterrows():
        table_cols.insert(parent="", index="end", values=row.tolist())


def update_interface():
    try:
        df = pd.read_excel("weather.xlsx")
        display_data(df)
    except Exception as error:
        print(error)

def generate_interface():
    root = tk.Tk()
    root.title("Nasza pierwsza aplikacja")
    root.geometry("800x600")
    load_button = tk.Button(root, text="Wybierz plik", command=load_excel_file)
    load_button.pack(padx=5)
    table_frame = tk.Frame(root)
    table_frame.pack(fill="both", expand=True, padx=10, pady=10)

    root.after(30000, lambda: update_interface(root))
    root.mainloop()