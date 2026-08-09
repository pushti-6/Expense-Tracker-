import sqlite3     
# id element should be primary and autoincrement
from datetime import datetime


DB_NAME="expenses.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS expenses(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        description TEXT NOT NULL,
        amount REAL NOT NULL,
        category TEXT NOT NULL,
        date TEXT NOT NULL
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS budget(
        id INTEGER PRIMARY KEY,
        amount REAL NOT NULL
    )
    """)

    conn.commit()
    conn.close()
    
def set_budget(amount):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("DELETE FROM budget")
    cursor.execute("INSERT INTO budget(amount) VALUES(?)",(amount,))

    conn.commit()
    conn.close()
def get_budget():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT amount FROM budget LIMIT 1")
    result = cursor.fetchone()

    conn.close()

    if result:
        return result[0]
    return 0
# to reset the table from 1 after all expenses are deleted
def reset_database():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # cursor.execute("DELETE FROM expenses")
    cursor.execute("DELETE FROM sqlite_sequence WHERE name='expenses'")

    conn.commit()
    conn.close()

    
def add_expense(description, amount, category):
    """Naya expense insert karne ke liye."""
    date_str = datetime.now().strftime("%Y-%m-%d")
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO expenses (description, amount, category, date) VALUES (?, ?, ?, ?)", 
                   (description, float(amount), category, date_str))
    conn.commit()
    conn.close()

def get_all_expenses():
    """Saare expenses nikalne ke liye."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM expenses ORDER BY id DESC")
    rows = cursor.fetchall()
    conn.close()
    return rows

def get_total_spent():
    """Saare expenses ka sum calculate karne ke liye."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT SUM(amount) FROM expenses")
    result = cursor.fetchone()[0]
    conn.close()
    return result if result is not None else 0.0

def delete_expense(expense_id):
    """Selected expense ko delete karne ke liye."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM expenses WHERE id = ?", (expense_id,))
    conn.commit()
    conn.close()
    


init_db()

