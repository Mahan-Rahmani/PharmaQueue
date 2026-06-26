import sqlite3
import tkinter as tk
from tkinter import messagebox
import ttkbootstrap as tb
from ttkbootstrap.constants import *

# Database setup
conn = sqlite3.connect("pharma_queue.db")
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS queue (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER,
    status TEXT
)
""")
conn.commit()

def get_priorities(status):
    status = status.lower()
    if status == 'emergency': return 1
    elif status == 'prescription': return 2
    else: return 3

class PharmaApp(tb.Window):
    def __init__(self):
        super().__init__(themename="flatly")
        self.title("PharmaQueue - Smart Management")
        self.geometry("600x650")

        # Title
        title_lbl = tb.Label(self, text="Pharmacy Queue Management System", font=("Arial", 20, "bold"), bootstyle="primary")
        title_lbl.pack(pady=20)

        # Input Panel
        input_frame = tb.LabelFrame(self, text="Patient Information")
        input_frame.pack(fill=X, padx=30, pady=10)

        # Adding widgets to the frame
        tb.Label(input_frame, text="Full Name:").grid(row=0, column=0, padx=10, pady=10)
        self.name_entry = tb.Entry(input_frame, width=30)
        self.name_entry.grid(row=0, column=1, padx=10, pady=10)

        tb.Label(input_frame, text="Age:").grid(row=1, column=0, padx=10, pady=10)
        self.age_entry = tb.Entry(input_frame, width=30)
        self.age_entry.grid(row=1, column=1, padx=10, pady=10)

        tb.Label(input_frame, text="Status:").grid(row=2, column=0, padx=10, pady=10)
        self.status_combo = tb.Combobox(input_frame, values=["General", "Emergency", "Prescription"], state="readonly", width=28)
        self.status_combo.current(0)
        self.status_combo.grid(row=2, column=1, padx=10, pady=10)

        # Buttons
        btn_frame = tb.Frame(self)
        btn_frame.pack(pady=10)

        tb.Button(btn_frame, text="Add to Queue", command=self.add_patient, bootstyle="success", width=15).grid(row=0, column=0, padx=5)
        tb.Button(btn_frame, text="Show List", command=self.show_list, bootstyle="info", width=15).grid(row=0, column=1, padx=5)
        tb.Button(btn_frame, text="Serve Patient", command=self.serve_patient, bootstyle="warning", width=15).grid(row=1, column=0, pady=10, padx=5)
        tb.Button(btn_frame, text="Search", command=self.search_patient, bootstyle="secondary", width=15).grid(row=1, column=1, pady=10, padx=5)

        # Display Table
        self.tree = tb.Treeview(self, columns=("ID", "Name", "Age", "Status"), show='headings', bootstyle="primary")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Name", text="Name")
        self.tree.heading("Age", text="Age")
        self.tree.heading("Status", text="Status")
        self.tree.column("ID", width=50)
        self.tree.pack(fill=BOTH, expand=True, padx=20, pady=20)

    def add_patient(self):
        try:
            cursor.execute("INSERT INTO queue (name, age, status) VALUES (?, ?, ?)", 
                           (self.name_entry.get(), int(self.age_entry.get()), self.status_combo.get()))
            conn.commit()
            messagebox.showinfo("Success", "Patient added successfully")
        except:
            messagebox.showerror("Error", "Please enter valid information")

    def show_list(self):
        for i in self.tree.get_children(): self.tree.delete(i)
        cursor.execute("SELECT * FROM queue")
        rows = sorted(cursor.fetchall(), key=lambda p: get_priorities(p[3]))
        for row in rows: self.tree.insert("", END, values=row)

    def serve_patient(self):
        cursor.execute("SELECT * FROM queue")
        rows = sorted(cursor.fetchall(), key=lambda p: get_priorities(p[3]))
        if rows:
            cursor.execute("DELETE FROM queue WHERE id = ?", (rows[0][0],))
            conn.commit()
            messagebox.showinfo("Serving", f"Now serving: {rows[0][1]}")
            self.show_list()
        else:
            messagebox.showwarning("Empty", "The queue is empty")

    def search_patient(self):
        name = self.name_entry.get()
        cursor.execute("SELECT * FROM queue WHERE LOWER(name) = LOWER(?)", (name,))
        results = cursor.fetchall()
        for i in self.tree.get_children(): self.tree.delete(i)
        for row in results: self.tree.insert("", END, values=row)

if __name__ == "__main__":
    app = PharmaApp()
    app.mainloop()