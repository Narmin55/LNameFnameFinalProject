import tkinter as tk
from tkinter import messagebox

class TourismApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Nermin Tourism")
        self.geometry("800x600")  # Pəncərə ölçüsünü təyin edir

        # Əsas səhifə komponentləri
        self.label_title = tk.Label(self, text="Nermin Tourism", font=("Helvetica", 16))
        self.label_title.place(relx=0.5, y=10, anchor="center")

        # Blog kartları
        self.frame_blog = tk.Frame(self)
        self.frame_blog.place(relx=0.5, rely=0.2, anchor="center")

        self.cards = []
        for _ in range(3):
            card = tk.Frame(self.frame_blog, padx=10, pady=10, width=200, height=200, relief="raised", borderwidth=2)
            card.grid(row=0, column=len(self.cards), padx=10, pady=10)

            label_state = tk.Label(card, text="A State Name", font=("Helvetica", 12, "bold"))
            label_state.pack()

            button_add_to_cart = tk.Button(card, text="Add to Cart", command=lambda c=card: self.add_to_cart(c))
            button_add_to_cart.pack()

            button_add_to_favorites = tk.Button(card, text="Add to Favorites", command=lambda c=card: self.add_to_favorites(c))
            button_add_to_favorites.pack()

            button_heart = tk.Button(card, text="❤️", command=lambda c=card: self.toggle_favorite(c))
            button_heart.pack()

            self.cards.append({"frame": card, "favorite": False, "heart_button": button_heart})

        # İdarə paneli komponentləri
        self.frame_admin = tk.Frame(self)
        self.frame_admin.place(relx=0.5, rely=0.8, anchor="center")

        label_admin_title = tk.Label(self.frame_admin, text="Admin Panel", font=("Helvetica", 12, "bold"))
        label_admin_title.grid(row=0, column=0, columnspan=2, pady=5)

        label_blog_title = tk.Label(self.frame_admin, text="Blog Title:")
        label_blog_title.grid(row=1, column=0, padx=5, pady=5)
        self.entry_blog_title = tk.Entry(self.frame_admin)
        self.entry_blog_title.grid(row=1, column=1, padx=5, pady=5)

        label_blog_content = tk.Label(self.frame_admin, text="Blog Content:")
        label_blog_content.grid(row=2, column=0, padx=5, pady=5)
        self.entry_blog_content = tk.Text(self.frame_admin, height=5, width=30)
        self.entry_blog_content.grid(row=2, column=1, padx=5, pady=5)

        button_add_blog = tk.Button(self.frame_admin, text="Add Blog", command=self.add_blog)
        button_add_blog.grid(row=3, column=0, columnspan=2, pady=5)

        # Footer komponenti
        self.label_footer = tk.Label(self, text="© 2024 Nermin Tourism. All rights reserved.", font=("Helvetica", 8))
        self.label_footer.place(relx=0.5, rely=0.95, anchor="center")

        # Navbar komponenti
        self.button_cart = tk.Button(self, text="Cart", command=self.show_cart)
        self.button_cart.place(relx=0.95, rely=0.05, anchor="e")

        # Ürək ikonası
        self.button_heart_icon = tk.Button(self, text="❤️", command=self.show_favorites)
        self.button_heart_icon.place(relx=0.05, rely=0.05, anchor="w")

    # Səbətə məhsul əlavə et
    def add_to_cart(self, card):
        messagebox.showinfo("Added to Cart", f"This card has been added to the cart.")

    # İstəklilərə məhsul əlavə et
    def add_to_favorites(self, card):
        index = next((i for i, item in enumerate(self.cards) if item["frame"] == card), None)
        if index is not None:
            self.cards[index]["favorite"] = not self.cards[index]["favorite"]
            if self.cards[index]["favorite"]:
                messagebox.showinfo("Added to Favorites", f"This card has been added to favorites.")
                self.cards[index]["heart_button"]["text"] = "❤️"
            else:
                messagebox.showinfo("Removed from Favorites", f"This card has been removed from favorites.")
                self.cards[index]["heart_button"]["text"] = "🖤"

    # Səbəti göstər
    def show_cart(self):
        messagebox.showinfo("Cart", "Items in the cart will be displayed here.")

    # Sevimliləri göstər
    def show_favorites(self):
        favorites = [card["frame"] for card in self.cards if card["favorite"]]
        if favorites:
            messagebox.showinfo("Favorites", "Your favorite items will be displayed here.")
        else:
            messagebox.showinfo("No Favorites", "You haven't added any items to favorites yet.")

    # Yeni blog əlavə et
    def add_blog(self):
        title = self.entry_blog_title.get()
        content = self.entry_blog_content.get("1.0", "end-1c")
        if title and content:
            messagebox.showinfo("Blog Added", f"The blog titled '{title}' has been added.")
            self.entry_blog_title.delete(0, tk.END)
            self.entry_blog_content.delete("1.0", tk.END)
            # Bu yerdə yeni bir blog kartı yaradıb əlavə edərik

app = TourismApp()
app.mainloop()
