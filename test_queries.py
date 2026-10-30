import sqlite3
import pytest
import queries
import sales_report

@pytest.fixture
def conn():
    conn = sqlite3.connect(":memory:")
    conn.row_factory = sqlite3.Row
    conn.executescript("""
        CREATE TABLE crm_customers (customer_id TEXT, name TEXT, city TEXT, segment TEXT);
        INSERT INTO crm_customers VALUES ('C1', 'Ravi Kumar', 'Pune', 'Retail');
        INSERT INTO crm_customers VALUES ('C2', 'Meera Rao', 'Pune', 'Wholesale');
        INSERT INTO crm_customers VALUES ('C3', 'Sana Khan', 'Delhi', 'Retail');
        CREATE TABLE invoices (invoice_id TEXT, billing_id TEXT, invoice_date TEXT, amount REAL, status TEXT);
        INSERT INTO invoices VALUES ('I1', 'B1', '2026-01-05', 1000.00, 'paid');
        INSERT INTO invoices VALUES ('I2', 'B1', '2026-01-20', 2000.50, 'unpaid');
        INSERT INTO invoices VALUES ('I3', 'B1', '2026-02-03',  500.00, 'paid');
        INSERT INTO invoices VALUES ('I4', 'B2', '2026-02-10', 3000.00, 'paid');
        INSERT INTO invoices VALUES ('I5', 'B3', '2026-02-15',  250.25, 'unpaid');
        INSERT INTO invoices VALUES ('I6', 'B3', '2026-03-01',  750.00, 'paid');
    """)
    yield conn
    conn.close()

def test_customers_in_city(conn):
    assert queries.customers_in_city(conn, "Pune") == [
        {"customer_id": "C2", "name": "Meera Rao", "segment": "Wholesale"},
        {"customer_id": "C1", "name": "Ravi Kumar", "segment": "Retail"},
    ]

def test_customers_in_city_rejects_injection(conn):
    assert queries.customers_in_city(conn, "Pune' OR '1'='1") == []

def test_invoice_totals_by_status(conn):
    assert queries.invoice_totals_by_status(conn) == { "paid": 5250.00, "unpaid": 2250.75 }

def test_monthly_invoices(conn):
    assert queries.monthly_invoices(conn) == [
        {"month": "2026-01", "invoices": 2, "total": 3000.50},
        {"month": "2026-02", "invoices": 3, "total": 3750.25},
        {"month": "2026-03", "invoices": 1, "total": 750.00},
    ]

@pytest.mark.parametrize("min_invoices, expected", [
    (1, 2),
    (2, 1),
    (3, 0),
])
def test_busy_accounts(conn, min_invoices, expected):
    assert queries.busy_accounts(conn, min_invoices) == expected

def test_customer_count(conn):
    assert queries.customer_count(conn) == 3

def test_customers_by_city(conn):
    assert queries.customers_by_city(conn) == [
        {"city": "Pune", "customers": 2},
        {"city": "Delhi", "customers": 1}
    ]

def test_customers_by_city_tie_sorted_by_name(conn):
    conn.execute("INSERT INTO crm_customers VALUES ('C4', 'Kiran Rao', 'Delhi', 'Retail')")
    assert queries.customers_by_city(conn) == [
        {"city": "Delhi", "customers": 2},
        {"city": "Pune", "customers": 2},
    ]

def test_customers_by_segment(conn):
    assert queries.customers_by_segment(conn) == [
        {"segment": "Retail", "customers": 2},
        {"segment": "Wholesale", "customers": 1}
    ]

def test_top_invoices(conn):
    assert queries.top_invoices(conn, 2) == [
        {"invoice_id": "I4", "billing_id": "B2", "amount": 3000, "status": "paid"},
        {"invoice_id": "I2", "billing_id": "B1", "amount": 2000.50, "status": "unpaid"}
    ]

def test_invoice_date_range(conn):
    assert queries.invoice_date_range(conn) == ("2026-01-05", "2026-03-01")

def test_invoice_date_range_empty(conn):
    conn.execute("DELETE FROM invoices")
    assert queries.invoice_date_range(conn) == (None, None)

def test_build_report(conn):
    report = sales_report.build_report(conn)
    assert "Total customers: 3" in report
    assert "Unpaid share: 30.0% of all invoicing" in report
    assert "Billing customers with more than 5 invoices: 0" in report

def test_build_report_no_invoices(conn):
    conn.execute("DELETE FROM invoices")
    report = sales_report.build_report(conn)
    assert "no invoices found" in report

def test_build_report_no_invoices(conn):
    conn.execute("DELETE FROM invoices")
    report = sales_report.build_report(conn)
    assert "no invoices found" in report