import tkinter as tk
from tkinter import messagebox

class LMS(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Library Management System")
        self.geometry("400x300")
        self.books = []
        self.label = tk.Label(self, text="Library Management System", font=("Helvetica", 16))
        self.label.pack(pady=10)
        self.title_label = tk.Label(self, text="Book Title:")
        self.title_label.pack()
        self.title_entry = tk.Entry(self)
        self.title_entry.pack()
        self.author_label = tk.Label(self, text="Author:")
        self.author_label.pack()
        self.author_entry = tk.Entry(self)
        self.author_entry.pack()
        self.add_button = tk.Button(self, text="Add Book", command=self.add_book)
        self.add_button.pack(pady=10)
        self.show_books_button = tk.Button(self, text="Show Books", command=self.show_books)
        self.show_books_button.pack(pady=10)
        self.quit_button = tk.Button(self, text="Quit", command=self.quit)
        self.quit_button.pack()
    def add_book(self):
        title = self.title_entry.get()
        author = self.author_entry.get()
        if title and author:
            self.books.append((title, author))
            messagebox.showinfo("Success", "Book added to the library.")
            self.title_entry.delete(0, tk.END)
            self.author_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Please enter both title and author.")
    def show_books(self):
        if not self.books:
            messagebox.showinfo("No Books", "No books in the library.")
        else:
            book_list = "\n".join([f"{i + 1}. {book[0]} by {book[1]}" for i, book in enumerate(self.books)])
            messagebox.showinfo("Books in Library", book_list)

app = LMS()
app.mainloop()
