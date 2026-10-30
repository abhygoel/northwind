"""Query functions for the Northwind database.

Every function expects a connection with row_factory = sqlite3.Row.
"""

def customers_in_city(conn, city):
    rows = conn.execute("""
        SELECT customer_id, name, segment 
        FROM crm_customers 
        WHERE city = ? 
        ORDER BY name ASC
    """, (city,)).fetchall()
    return [dict(row) for row in rows]

def invoice_totals_by_status(conn):
    rows = conn.execute("""
        SELECT status, ROUND(SUM(amount), 2) AS total
        FROM invoices 
        GROUP BY status
    """).fetchall()
    return {row["status"]: row["total"] for row in rows}

def monthly_invoices(conn):
    rows = conn.execute("""
        SELECT SUBSTR(invoice_date, 1, 7) AS month, COUNT(*) AS invoices, ROUND(SUM(amount), 2) AS total
        FROM invoices
        GROUP BY month
        ORDER BY month ASC
    """).fetchall()
    return [dict(row) for row in rows] 

def busy_accounts(conn, min_invoices):
    return conn.execute("""
        SELECT COUNT(*) AS customers
        FROM (
            SELECT billing_id, COUNT(*)
            FROM invoices
            GROUP BY billing_id
            HAVING COUNT(*) > ? )
    """, (min_invoices,)).fetchone()["customers"]

def customer_count(conn):
    return conn.execute("""
        SELECT COUNT(*) AS customers
        FROM crm_customers
    """).fetchone()["customers"]

def customers_by_city(conn):
    rows = conn.execute("""
        SELECT city, COUNT(*) AS customers 
        FROM crm_customers 
        GROUP BY city
        ORDER BY customers DESC, city
    """).fetchall()
    return [dict(row) for row in rows]

def customers_by_segment(conn):
    rows = conn.execute("""
        SELECT segment, COUNT(*) AS customers 
        FROM crm_customers 
        GROUP BY segment
        ORDER BY customers DESC, segment
    """).fetchall()
    return [dict(row) for row in rows]

def top_invoices(conn, limit):
    rows = conn.execute("""
        SELECT invoice_id, billing_id, amount, status
        FROM invoices
        ORDER BY amount DESC, invoice_id
        LIMIT ?
    """, (limit,)).fetchall()
    return [dict(row) for row in rows] 

def invoice_date_range(conn):
    row = conn.execute("""
        SELECT MIN(invoice_date), MAX(invoice_date)
        FROM invoices
    """).fetchone()
    return tuple(row)
