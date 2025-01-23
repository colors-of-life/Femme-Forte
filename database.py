import sqlite3

# Connect to database
conn = sqlite3.connect("example.db")
cursor = conn.cursor()

# Create table
cursor.execute(f"""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    email TEXT UNIQUE,
    face INTEGER
)
""")

# Insert data
cursor.execute("""
INSERT INTO users (name, age, email, face)
VALUES (?, ?, ?, ?)
""", ("Alice", 25, "alice@example.com", None))

# Commit changes
conn.commit()

# Query data
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()

# Display data
for row in rows:
    print(row)

# Close connection
conn.close()
