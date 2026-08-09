# Expense-Tracker-
# 💰 Expense Tracker

A simple and user-friendly **Expense Tracker desktop application** built using **Python, CustomTkinter, Tkinter, and SQLite/database functionality**.

The application provides a graphical interface for adding, viewing, and deleting expenses while keeping track of total spending. It also includes expense categories, a monthly budget section, a savings goal section, a calendar, and a Dark Mode option.

---

## ✨ Features

* ➕ **Add Expenses**

  * Enter an expense description
  * Enter the expense amount
  * Select an expense category
  * Validate that the amount is a positive number

* 📋 **Expense Table**

  * Displays saved expenses
  * Shows expense ID, description, category, and amount
  * Includes a vertical scrollbar

* 🗑️ **Delete Expenses**

  * Select an expense from the table
  * Delete it after confirmation

* 💵 **Total Expenses**

  * Automatically calculates and displays the total amount spent

* 📊 **Monthly Budget**

  * Allows the user to enter a monthly budget
  * Calculates the remaining amount based on total expenses

* 🎯 **Savings Goal**

  * Provides an input field for setting a savings goal

* 📅 **Calendar**

  * Integrated calendar using `tkcalendar`
  * Allows the user to select a date

* 🌙 **Dark Mode**

  * Switch between Light Mode and Dark Mode

* 🎨 **Modern GUI**

  * Built using CustomTkinter
  * Responsive two-section layout with sidebar and main content area

---

## 🛠️ Technologies Used

| Technology      | Purpose                                  |
| --------------- | ---------------------------------------- |
| Python          | Main programming language                |
| CustomTkinter   | Modern graphical user interface          |
| Tkinter         | GUI components and message boxes         |
| ttk             | Treeview table and scrollbar             |
| tkcalendar      | Calendar widget                          |
| Database module | Stores and retrieves expense information |

---

## 📁 Project Structure

```text
Expense-Tracker/
│
├── main.py
├── database.py
├── README.md
└── requirements.txt
```

> Rename `main.py` to whatever filename you use for the uploaded application code.

---

## 📦 Requirements

Make sure **Python 3.9 or newer** is installed.

The project requires the following external Python packages:

```text
customtkinter
tkcalendar
```

Tkinter and `ttk` are normally included with standard Python installations.

---

## 🚀 Installation

### 1. Clone or download the project

Download the project files and open the project folder in VS Code or another Python IDE.

### 2. Create a virtual environment

Open a terminal inside the project folder:

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 3. Install the required packages

```bash
pip install customtkinter tkcalendar
```

Alternatively, if a `requirements.txt` file is included:

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Application

Run the main Python file:

```bash
python main.py
```

The Expense Tracker window should open automatically.

The application starts through:

```python
app = ExpenseTrackerApp()
app.mainloop()
```

---

## 🖥️ Application Layout

The application is divided into two major sections.

### Sidebar

The sidebar contains:

* Application title
* Add Expense section
* Description input
* Amount input
* Category selection
* Add Expense button
* Monthly Budget input
* Savings Goal input
* Save Goal button
* Dark Mode switch

The application provides predefined categories including:

* Food and Drinks
* Books & Stationery
* Clothing & Accessories
* Electronics & Gadgets
* Health & Fitness
* Home & Living
* Personal Care & Beauty
* Sports & Outdoor Activities
* Transportation & Travel
* Other

### Main Content Area

The main area contains:

* Total Expenses card
* Expense table
* Delete button
* Calendar

---

## ➕ Adding an Expense

To add a new expense:

1. Enter the expense description.
2. Enter the amount.
3. Select a category.
4. Click **Add new Expense**.

The application checks that all required fields are filled and that the amount is a valid positive number before saving the expense.

---

## 🗑️ Deleting an Expense

To delete an expense:

1. Select the expense from the table.
2. Click **DELETE**.
3. Confirm the deletion.

The selected expense is then removed from the database and the interface is refreshed.

---

## 💰 Budget Tracking

The application includes a **Monthly Budget** field.

After entering a budget, the application uses the total expenses to calculate the remaining amount:

```text
Remaining Budget = Monthly Budget - Total Expenses
```

---

## 📅 Calendar

A calendar is included using the `tkcalendar` package.

The calendar uses the following date format:

```text
DD-MM-YYYY
```

Users can select a date from the calendar interface.

---

## 🌙 Dark Mode

The application starts in Light Mode.

The **Dark Mode** switch changes the CustomTkinter appearance between:

```text
Light
Dark
```

---

## 🗄️ Database

The application imports a separate database module:

```python
import database as db
```

The database module is responsible for operations such as:

```python
db.add_expense()
db.delete_expense()
db.get_all_expenses()
db.get_total_spent()
db.set_budget()
db.get_budget()
```

Therefore, `database.py` must be present in the same project directory for the application to work correctly.

---

## ⚠️ Important Notes

Make sure the following files are present:

```text
main.py
database.py
```

The GUI code depends on `database.py` for storing and retrieving expense information.

The current implementation also contains some features that may require additional connection/implementation work, such as the **Save Goal** button and selected-calendar-date handling.

---

## 🔮 Future Improvements

Possible improvements include:

* 📈 Expense charts and graphs
* 📊 Category-wise spending analysis
* 🔍 Search and filter expenses
* 📅 Store expense dates in the database
* 🎯 Fully implement savings-goal tracking
* 💾 Export expenses to CSV or Excel
* 📱 Improve responsive layout
* 🔐 Add user accounts/login
* 📆 Monthly and yearly expense reports
* 💡 Budget alerts when spending exceeds the budget

---

## 👩‍💻 Author

**Expense Tracker Project**

Built using Python and CustomTkinter.

---

## 📄 License

This project is intended for educational and personal use.
