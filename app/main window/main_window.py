import ttkbootstrap as ttk
from tkinter import messagebox
from ttkbootstrap.window import Window
import tkinter as tk

import sys
import os

# Get the directory of the current script (main_window.py)
current_dir = os.path.dirname(os.path.abspath(__file__))

# Add the root directory to sys.path (parent of the current directory)
project_root = os.path.dirname(os.path.dirname(current_dir))
print("Project root:", project_root)
sys.path.append(project_root)

# Now try importing
from search.search import search_whole_sheet

class App:
    def __init__(self):
        # Cria a janela principal
        self.win = Window(themename='journal')
        self.win.title('App')
        self.__start__()

    def __start__(self):
        self.set_geometry()
        search(self.win)
        self.win.mainloop()  # Iniciar o loop principal da aplicação

    def set_geometry(self):
        # Definir o tamanho da janela
        window_width = 1000
        window_height = 600

        # Obtém as dimensões da tela
        display_width = self.win.winfo_screenwidth()
        display_height = self.win.winfo_screenheight()

        # Calcula a posição da janela para ficar centralizada
        left = int(display_width / 2 - window_width / 2)
        top = int(display_height / 2 - window_height / 2)

        # Define a geometria da janela
        self.win.geometry(f'{window_width}x{window_height}+{left}+{top}')
        self.win.minsize(500, 300)

def search(app: ttk.Window):
    data = []

    def search_action(event=None):  # Add event parameter with a default value
        query = search_entry.get()
        print(f"Search Query: {query}")
        nonlocal data  # Ensure data is accessible within this scope
        data = search_whole_sheet(r'test\files\DADOS FINANCEIROS - 2025.xlsx', query)
        print("Search Results:", data)
        display()

    search_label = ttk.Label(app, text='Search:', font=('Helvetica', 12))
    search_label.grid(row=0, column=0, columnspan=2, sticky='nsw', padx=10, pady=10)

    search_entry = ttk.Entry(app, bootstyle="info", width=50)
    search_entry.grid(row=0, column=2, columnspan=1, sticky='nsew', padx=10, pady=10)
    search_entry.bind('<Return>', search_action)

    search_btn = ttk.Button(app, text='Search', bootstyle='success', command=search_action)
    search_btn.grid(row=0, column=3, columnspan=2, sticky='nse', padx=10, pady=10)

    def adjust_listbox_height(listbox, row_count):
        # Set the height based on the number of rows
        listbox.config(height=min(row_count, 50))  # Max height of 10 rows

    def adjust_listbox_width(listbox, data):
        # Calculate the maximum width needed for each column
        max_widths = [max(len(str(item)) for item in column) for column in zip(*data)]

        # Calculate the total width by summing the maximum widths of all columns
        total_width = sum(max_widths) + len(max_widths) - 1  # Add space for separators

        # Set the width of the Listbox based on the calculated total width
        listbox.config(width=total_width)

    def display():
        # Clear the Listbox
        result_listbox.delete(0, tk.END)

        # Filter the data based on search_value and display the results
        filtered_data = data

        for row in filtered_data:
            # Convert each item in the row to a string before joining
            row_str = [str(item) for item in row]
            result_listbox.insert(tk.END, " | ".join(row_str))

        # Adjust the Listbox height based on the number of filtered rows
        adjust_listbox_height(result_listbox, len(filtered_data))

        # Adjust the Listbox width based on the content
        #adjust_listbox_width(result_listbox, filtered_data)

    result_listbox = tk.Listbox(app)
    result_listbox.grid(row=1, column=0, columnspan=5, sticky='nsew', padx=10, pady=10)

    def on_row_select(event):
        # Get the index of the clicked item
        select_index = result_listbox.curselection()

        if select_index:
            if event.num == 1:  # Left click
                print("Left Clicked on:", data[select_index[0]])
            elif event.num == 3:  # Right click
                row_data = data[select_index[0]]
                messagebox.showinfo("Row Data", f"Selected Row: {row_data}")

    # Bind left and right-click events to the Listbox
    result_listbox.bind('<Button-1>', on_row_select)  # Left click
    result_listbox.bind('<Button-3>', on_row_select)  # Right click

    def selected_row():
        select_index = result_listbox.curselection()
        if select_index:
            row_data = data[select_index[0]]
            print(row_data)

    select_btn = ttk.Button(app, text='Select', bootstyle='success', command=selected_row)
    select_btn.grid(row=2, column=0, columnspan=5, sticky='new', padx=10, pady=10)




# Execução da aplicação
if __name__ == "__main__":
    app = App()
