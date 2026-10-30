import argparse
import os
import sqlite3
import sys
from pathlib import Path
import queries
from datetime import date

def build_report(conn):
    lines = []
    lines.append("# Northwind sales report")
    lines.append("")
    lines.append(f"Generated: {date.today()}")
    lines.append("")

    first, last = queries.invoice_date_range(conn)
    if first is None:
        lines.append("Data covered: no invoices found.")
    else:
        lines.append(f"Data covered: {first} to {last}")
    lines.append("")

    lines.append("## Customers")
    lines.append("")
    customer_count = queries.customer_count(conn)
    lines.append(f"Total customers: {customer_count:,}")
    lines.append("")

    lines.append("### By city")
    lines.append("")
    lines.append("| City | Customers |")
    lines.append("|---|---|")
    for row in queries.customers_by_city(conn):
        lines.append(f"| {row['city']} | {row['customers']:,} |")
    lines.append("")

    lines.append("### By segment")
    lines.append("")
    lines.append("| Segment | Customers |")
    lines.append("|---|---|")
    for row in queries.customers_by_segment(conn):
        lines.append(f"| {row['segment']} | {row['customers']:,} |")
    lines.append("")

    lines.append("## Invoicing")
    lines.append("")
    lines.append("| Status | Total (₹) |")
    lines.append("|---|---|")
    totals = queries.invoice_totals_by_status(conn)
    for status, total in totals.items():
        lines.append(f"| {status.title()} | {total:,.2f} |")
    lines.append("")

    unpaid = totals.get("unpaid", 0)
    all_invoicing = sum(totals.values())
    if all_invoicing > 0:
        share = unpaid / all_invoicing * 100
        lines.append(f"Unpaid share: {share:.1f}% of all invoicing")
        lines.append("")

    lines.append("## Monthly invoicing")
    lines.append("")
    lines.append("| Month | Invoices | Total (₹) |")
    lines.append("|---|---|---|")
    months = queries.monthly_invoices(conn)
    for row in months:
        lines.append(f"| {row['month']} | {row['invoices']:,} | {row['total']:,.2f} |")
    lines.append("")
    if months:
        last_month = months[-1]["month"]
        lines.append(f"Note: data ends on {last}, so {last_month} may be incomplete.")
        lines.append("")

    lines.append("## Top 10 invoices")
    lines.append("")
    lines.append("| Invoice | Billing ID | Amount (₹) | Status |")
    lines.append("|---|---|---|---|")
    for row in queries.top_invoices(conn, 10):
        lines.append(f"| {row['invoice_id']} | {row['billing_id']} | {row['amount']:,.2f} | {row['status']} |")
    lines.append("")

    lines.append("## Busy accounts")
    lines.append("")
    busy_accounts = queries.busy_accounts(conn, 5)
    lines.append(f"Billing customers with more than 5 invoices: {busy_accounts:,}")
    lines.append("")
    return "\n".join(lines)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create Northwind sales report.")
    parser.add_argument("input_db", help="The db to get data")
    parser.add_argument("--output", default="sales_report.md", help="Output file")
    args = parser.parse_args()
    if not os.path.exists(args.input_db):
        print(f"Database {args.input_db} doesn't exist.")
        sys.exit(1)
    conn = sqlite3.connect(args.input_db)
    conn.row_factory = sqlite3.Row
    report = build_report(conn)
    conn.close()
    Path(args.output).write_text(report, encoding="utf-8")
    print(f"Report saved to {args.output}")