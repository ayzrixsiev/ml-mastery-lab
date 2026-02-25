import sqlite3

conn = sqlite3.connect("finance.db")
cursor = conn.cursor()

cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS transactions(
            id INTEGER PRIMARY KEY,
            category TEXT,
            amount REAL,
            month TEXT
    )
"""
)
data = [
    # JANUARY
    ("Rent", 1200.00, "January"),
    ("Groceries", 155.50, "January"),
    ("Electricity Bill", 85.00, "January"),
    ("Internet", 60.00, "January"),
    ("Coffee Shop", 12.00, "January"),
    ("Netflix Subscription", 15.99, "January"),
    ("Gasoline", 55.00, "January"),
    # FEBRUARY
    ("Rent", 1200.00, "February"),
    ("Groceries", 142.00, "February"),
    ("Electricity Bill", 90.00, "February"),
    ("Gym Membership", 50.00, "February"),
    ("New Laptop", 850.00, "February"),
    ("Dinner Out", 75.00, "February"),
    ("Gasoline", 48.00, "February"),
    # MARCH
    ("Rent", 1200.00, "March"),
    ("Groceries", 168.00, "March"),
    ("Electricity Bill", 78.00, "March"),
    ("Internet", 60.00, "March"),
    ("Concert Tickets", 120.00, "March"),
    ("Pharmacy", 35.00, "March"),
    ("Gasoline", 62.00, "March"),
    # APRIL
    ("Rent", 1200.00, "April"),
    ("Groceries", 145.00, "April"),
    ("Electricity Bill", 72.00, "April"),
    ("Car Insurance", 110.00, "April"),
    ("Amazon - Headphones", 99.00, "April"),
    ("Coffee Shop", 8.50, "April"),
    ("Gasoline", 50.00, "April"),
]
cursor.executemany(
    "INSERT INTO transactions (category, amount, month) VALUES (?, ?, ?)", data
)

conn.commit()
conn.close()
print("Database 'finance.db' created successfully!")
