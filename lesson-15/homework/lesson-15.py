import sqlite3

# Connect to a new SQLite database (or open if exists)
conn = sqlite3.connect('starfleet.db')
cursor = conn.cursor()

# 1. Create the Roster table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Roster (
    Name TEXT,
    Species TEXT,
    Age INTEGER
)
''')

# 2. Insert initial data
roster_data = [
    ("Benjamin Sisko", "Human", 40),
    ("Jadzia Dax", "Trill", 300),
    ("Kira Nerys", "Bajoran", 29)
]

# Clear the table to avoid duplicate entries if re-running
cursor.execute("DELETE FROM Roster")

cursor.executemany('''
INSERT INTO Roster (Name, Species, Age)
VALUES (?, ?, ?)
''', roster_data)

# 3. Update Jadzia Dax to Ezri Dax
cursor.execute('''
UPDATE Roster
SET Name = 'Ezri Dax'
WHERE Name = 'Jadzia Dax'
''')

# 4. Query and display Name and Age of Bajoran individuals
cursor.execute('''
SELECT Name, Age FROM Roster
WHERE Species = 'Bajoran'
''')

bajoran_members = cursor.fetchall()

print("Bajoran Roster:")
for name, age in bajoran_members:
    print(f"Name: {name}, Age: {age}")

# Save changes and close connection
conn.commit()
conn.close()
