import requests
from bs4 import BeautifulSoup
import sqlite3

# Step 1: Scrape the links
req = requests.get("https://www.geeksforgeeks.org/dsa-tutorial-learn-data-structures-and-algorithms/")
soup = BeautifulSoup(req.content, 'html.parser')

s = soup.find('div')  # Adjust if you want to target specific divs
links = s.find_all('a')  # Find all <a> tags to extract href attributes

# Step 2: Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect("scraped_data.db")
cursor = conn.cursor()

# Step 3: Create a table to store the links
cursor.execute("""
CREATE TABLE IF NOT EXISTS links (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    url TEXT NOT NULL
)
""")

# Step 4: Insert scraped links into the database
for link in links:
    href = link.get('href')  # Extract the href attribute
    if href:  # Check if the href exists
        cursor.execute("INSERT INTO links (url) VALUES (?)", (href,))

# Commit the transaction
conn.commit()

# Step 5: Fetch and display the contents of the table
print("\n--- Saved Links in Database ---")
cursor.execute("SELECT * FROM links")
rows = cursor.fetchall()

for row in rows:
    print(row)

# Step 6: Close the connection
conn.close()
