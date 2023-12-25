import tkinter as tk
from tkinter import Toplevel, messagebox
import random
from datetime import datetime

class LibraryApp:
    def show_book_details(self, author, title, book_number):
      book_info = f"Книга: {title}, Автор: {author}, Номер: {book_number} Власник: {'Бібліотека'}"
      messagebox.showinfo("Деталі книги", book_info)

    def __init__(self, root):
        self.root = root
        self.root.title("Бібліотека")
        self.root.geometry("600x600")

        #словник для збереження інформації про книги та отримувачів
        self.books = []
        self.borrowers = []
        
        self.create_widgets()

    def create_widgets(self): #список зліва
        
        frame_left = tk.Frame(self.root, bg="lightgrey", width=300, height=600)
        frame_left.pack_propagate(False)
        frame_left.pack(side=tk.LEFT, fill=tk.BOTH)

        #кнопки до лівого фрейму
        btn_add_book = tk.Button(frame_left, text="Додати книгу", command=self.open_add_book_window)
        btn_add_book.pack(pady=20)

        btn_borrow_book = tk.Button(frame_left, text="Видати книгу", command=self.open_borrow_book_window)
        btn_borrow_book.pack(pady=20)

        

    def open_add_book_window(self): #додавання книжки 
        add_book_window = Toplevel(self.root)
        add_book_window.title("Додати книгу")

       
        label_author = tk.Label(add_book_window, text="Автор:")
        label_author.grid(row=0, column=0, padx=10, pady=10)

        entry_author = tk.Entry(add_book_window)
        entry_author.grid(row=0, column=1, padx=10, pady=10)

        label_title = tk.Label(add_book_window, text="Назва книги:")
        label_title.grid(row=1, column=0, padx=10, pady=10)

        entry_title = tk.Entry(add_book_window)
        entry_title.grid(row=1, column=1, padx=10, pady=10)

        btn_ok = tk.Button(add_book_window, text="ОК", command=lambda: self.add_book_callback(entry_author.get(), entry_title.get(), add_book_window))
        btn_ok.grid(row=2, column=0, columnspan=2, pady=20)

    def add_book_callback(self, author, title, add_book_window):
        if author and title:
            # Зберігаємо інформацію про книгу у словнику та відображаємо кнопку
            book_number = random.randint(1000, 9999)
            book_info = {'author': author, 'title': title, 'number': book_number, 'borrower': None}
            self.books.append(book_info)

            #кнопка для нової книги 
            btn_book = tk.Button(self.root, text=f"{author} - {title}, Номер: {book_number}", command=lambda: self.show_book_details(author, title, book_number))
            btn_book.pack(side=tk.TOP, fill=tk.X, pady=5)

            messagebox.showinfo("Успіх", f"Додано книгу: {author} - {title}, Номер: {book_number}")
            add_book_window.destroy()
        else:
            messagebox.showerror("Помилка", "Будь ласка, введіть автора та назву книги.")

    def open_borrow_book_window(self):#видача книжки
        borrow_book_window = Toplevel(self.root)
        borrow_book_window.title("Видати книгу")

        
        label_book_number = tk.Label(borrow_book_window, text="Номер книги:")
        label_book_number.grid(row=0, column=0, padx=10, pady=10)

        entry_book_number = tk.Entry(borrow_book_window)
        entry_book_number.grid(row=0, column=1, padx=10, pady=10)

        label_borrower_name = tk.Label(borrow_book_window, text="Ім'я та прізвище отримувача:")
        label_borrower_name.grid(row=1, column=0, padx=10, pady=10)

        entry_borrower_name = tk.Entry(borrow_book_window)
        entry_borrower_name.grid(row=1, column=1, padx=10, pady=10)

        btn_ok = tk.Button(borrow_book_window, text="ОК", command=lambda: self.borrow_book(entry_book_number.get(), entry_borrower_name.get(), borrow_book_window))
        btn_ok.grid(row=2, column=0, columnspan=2, pady=20)

    def borrow_book(self, book_number, borrower_name, borrow_book_window):#тоже видача книжки
        try:
            book_number = int(book_number)
            book_info = next(book for book in self.books if book['number'] == book_number)
            borrower = {'name': borrower_name, 'date': datetime.now().strftime("%Y-%m-%d")}
            book_info['borrower'] = borrower
            self.borrowers.append(borrower)

            messagebox.showinfo("Успіх", f"Книга видана {borrower_name} з номером {book_number}.\nДата видачі: {borrower['date']}")
            borrow_book_window.destroy()

        except StopIteration:
            messagebox.showerror("Помилка", f"Книги з номером {book_number} не існує.")
        except ValueError:
            messagebox.showerror("Помилка", "Будь ласка, введіть коректний номер книги.")

    

if __name__ == "__main__":
    root = tk.Tk()
    app = LibraryApp(root)
    root.mainloop()

