# 🛒 Mini Product System

> A tiny command-line shop assistant that lives in your terminal.
> No browser. No database. No drama. Just products, prices, and a menu.

---

## ✨ What is this?

**Mini Product System** is a lightweight Python console app for browsing and
exploring a product catalog. Think of it as a pocket-sized store manager: you
type a number, and it does the digging for you.

Perfect for practicing Python fundamentals like functions, loops, sorting,
and searching.

---

## 🧭 The Menu

When you launch the app, you'll see this:

```
================================
     MINI PRODUCT SYSTEM
================================

1. Show all products
2. Sort by price (ascending)
3. Sort by price (descending)
4. Search product by name
5. Search product by ID
6. Find the cheapest product
7. Find the most expensive product

0. Exit

================================
```

*(The in-app labels are in Azerbaijani. Translating them is a great first
contribution!)*

| Option | What it does                                     |
|:------:|--------------------------------------------------|
| `1`    | Lists every product in the catalog               |
| `2`    | Sorts products from cheapest to priciest         |
| `3`    | Sorts products from priciest to cheapest         |
| `4`    | Finds a product by its name                      |
| `5`    | Finds a product by its unique ID                 |
| `6`    | Reveals the budget-friendly champion             |
| `7`    | Reveals the luxury king                          |
| `0`    | Closes the program                               |

---

## 🚀 Getting Started

### Requirements
- Python 3.x

### Run it

```bash
git clone <your-repo-url>
cd <your-project-folder>
python main.py
```

Then type a number and press **Enter**. That's it.

---

## 🗂️ Project Structure

```
.
├── main.py         # The menu and the main loop (the "face" of the app)
├── functions.py    # All the logic: show, sort, search, min/max (the "brain")
└── README.md       # You are here 👋
```

- **`main.py`** keeps the program alive in a `while True` loop, shows the
  menu, reads your choice, and calls the right function.
- **`functions.py`** holds the functions that do the real work:
  `showproducts`, `sortbypriceasc`, `sortbypricedesc`, `searchbyname`,
  `searchbyid`, `getcheapestproduct`, `getexpensiveproduct`.

---

## 🧠 How It Works

```
        ┌────────────┐
        │ Show menu  │
        └─────┬──────┘
              ▼
        ┌────────────┐
        │ Your choice│
        └─────┬──────┘
              ▼
   ┌──────────┴──────────┐
   │  Matching function  │
   │   in functions.py   │
   └──────────┬──────────┘
              ▼
        ┌────────────┐
        │Print result│──► back to the menu
        └────────────┘
```

Type `0` to break the loop and say goodbye. Type anything unexpected and the
app politely tells you the choice was invalid, then shows the menu again.

---

## 🌱 Ideas for Future Upgrades

- ➕ Add, edit, and delete products
- 💾 Save products to a JSON or CSV file
- 🔎 Partial-match and case-insensitive search
- 🌍 Switch the interface between Azerbaijani and English
- 🎨 Colorful terminal output
- 🧪 Unit tests for every function

---

## 🤝 Contributing

Found a bug? Have a cool idea? Open an issue or send a pull request.
Every little improvement makes the system a little less "mini".

---

## 📄 License

Free to use, study, and remix. Happy coding! 💻☕
