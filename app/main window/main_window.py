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

app_active = None
def start_app():
    global app_active

    if app_active is not None and ttk.Toplevel.winfo_exists(app_active):
        app_active.lift()
        return

    app_active = Window(themename='journal')
    app_active.title('App')

    # Dimensions
    display_width = app_active.winfo_screenwidth()
    display_height = app_active.winfo_screenheight()

    window_width = int(display_width / 2)
    window_height = int(display_height / 2)

    # Calculate the position to center the window
    left = int(display_width / 2 - window_width / 2)
    top = int(display_height / 2 - window_height / 2)

    app_active.geometry(f'{window_width}x{window_height}+{left}+{top}')
    app_active.minsize(500, 300)

    # ________________________________________________________________
    # ________________________________________________________________
    # ________________________________________________________________

    # Search Module
    # Screen 5 Columns

    excel_data = []

    search_label = ttk.Label(app_active, text='Search', font=('Arial', 12))
    search_label.grid(row=0, column=0, columnspan=1, sticky='nsw', padx=5, pady=10)

    search_entry = ttk.Entry(app_active, bootstyle="info", width=50)
    search_entry.grid(row=0, column=1, columnspan=3, sticky='nsew', padx=5, pady=10)

    app_active.mainloop()

def search(app: ttk.Window):
    data = []

    def search_action(event=None):  # Add event parameter with a default value
        query = search_entry.get()
        print(f"Search Query: {query}")
        nonlocal data  # Ensure data is accessible within this scope
        data = search_whole_sheet(r'test\files\DADOS FINANCEIROS - 2025.xlsx', query)
        print("Search Results:", data)
        display_search()
        print("Returned Row Data:", row_data)

    search_label = ttk.Label(app, text='Search:', font=('Helvetica', 12))
    search_label.grid(row=0, column=0, columnspan=2, sticky='nsw', padx=10, pady=10)

    search_entry = ttk.Entry(app, bootstyle="info", width=50)
    search_entry.grid(row=0, column=2, columnspan=1, sticky='nsew', padx=10, pady=10)
    search_entry.bind('<Return>', search_action)

    search_btn = ttk.Button(app, text='Search', bootstyle='success', command=search_action)
    search_btn.grid(row=0, column=3, columnspan=2, sticky='nse', padx=10, pady=10)

    def adjust_listbox_height(listbox, row_count):
        # Set the height based on the number of rows
        listbox.config(height=min(row_count, 50))  # Max height of 50 rows

    def adjust_listbox_width(listbox, data):
        # Calculate the maximum width needed for each column
        max_widths = [max(len(str(item)) for item in column) for column in zip(*data)]

        # Calculate the total width by summing the maximum widths of all columns
        total_width = sum(max_widths) + len(max_widths) - 1  # Add space for separators

        # Set the width of the Listbox based on the calculated total width
        listbox.config(width=total_width)

    def display_search():
        # Clear the Listbox
        result_listbox.delete(0, tk.END)

        # Filter the data and display the results
        filtered_data = data

        for row in filtered_data:
            # Convert each item in the row to a string before joining
            row_str = [str(item) for item in row]
            result_listbox.insert(tk.END, " | ".join(row_str))

        # Adjust the Listbox height based on the number of filtered rows
        adjust_listbox_height(result_listbox, len(filtered_data))

        # Bind the row selection function to return the selected row's data
        def on_row_select(event):
            select_index = result_listbox.curselection()
            if select_index:
                row_data = filtered_data[select_index[0]]
                print("Row Data Selected:", row_data)
                return row_data

        result_listbox.bind('<Button-1>', on_row_select)  # Bind left click to select row

        return None  # Return None if no selection is made

    result_listbox = tk.Listbox(app)
    result_listbox.grid(row=1, column=0, columnspan=5, sticky='nsew', padx=10, pady=10)

    row_data = []
    def selected_row():
        select_index = result_listbox.curselection()
        if select_index:
            row_data = data[select_index[0]]
            print(row_data)

    select_btn = ttk.Button(app, text='Select', bootstyle='success', command=selected_row)
    select_btn.grid(row=2, column=0, columnspan=5, sticky='new', padx=10, pady=10)
    return row_data


# Run the application
if __name__ == "__main__":
    app = App()
