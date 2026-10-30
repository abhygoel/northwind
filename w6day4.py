import sqlite3
import pytest


conn = sqlite3.connect("northwind.db")
rows = conn.execute("SELECT city, COUNT(*) FROM crm_customers GROUP BY city").fetchall()
conn.close()

for city, count in rows:
    print(city, count)

conn = sqlite3.connect("northwind.db")
conn.row_factory = sqlite3.Row
row = conn.execute("SELECT * FROM crm_customers LIMIT 1").fetchone()
print(row["name"], row["city"])
print(dict(row))



city = "Pune"
# Dangerous:
# conn.execute(f"SELECT name FROM crm_customer WHERE city = '{city}'")
# safe
conn.execute("SELECT name FROM crm_coustomer WHEER city = ?", (city,))

@pytest.fixture
def conn():
    conn = sqlite3.connect(":memory:")
    conn.row_factory = sqlite3.Row
    conn.executescript("""
        CREATE TABLE crm_customers (customer_id TEXT, name TEXT, city TEXT, segment TEXT);
        INSERT INTO crm_customers VALUES ('C1', 'Ravi Kumar', 'Pune', 'Retail');
        INSERT INTO crm_customers VALUES ('C2', 'Meera Rao', 'Pune', 'Wholesale');
        INSERT INTO crm_customers VALUES ('C3', 'Sana Khan', 'Delhi', 'Retail');
    """)
    yield conn
    conn.close()

conn = sqlite3.connect("northwind.db")
conn.row_factory = sqlite3.Row
rows = conn.execute("SELECT city, COUNT(*) AS customers FROM crm_customers GROUP BY city").fetchall()
conn.close()
for row in rows:
    print(row["city"], row["customers"])

conn = sqlite3.connect("northwind.db")
city = "Pune' OR '1'='1"
rows = conn.execute("SELECT COUNT(*) FROM crm_customers WHERE city = ?", (city, )).fetchall()
conn.close()
print(rows)