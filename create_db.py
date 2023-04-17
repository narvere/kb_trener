import sqlite3

# Connect to database
conn = sqlite3.connect("keyboard_trainer.sql3")

# Create a table
conn.execute('''CREATE TABLE IF NOT EXISTS my_records (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            finger TEXT NOT NULL,
            main_letter TEXT NOT NULL,
            letters_list TEXT NOT NULL,
            num_letters INT NOT NULL,
            records TEXT NULL)''')

# # Add finger 'правый указательный'
# conn.execute("INSERT INTO my_records (finger) VALUES ('правый указательный')")

print("База создана!")
# Save changes
conn.commit()

# Close connection
conn.close()
