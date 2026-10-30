-- Aggregate
SELECT COUNT(*), SUM(amount), AVG(amount), MIN(amount), MAX(amount)
FROM invoices;

-- AS, ROUND
SELECT ROUND(SUM(amount), 2) AS total_invoiced
FROM invoices;

--GROUP BY
SELECT city, segment, COUNT(*) AS customers
FROM crm_customers
GROUP BY city, segment
ORDER BY city, customers;

--HAVING
SELECT billing_id, COUNT(*) AS invoice_count
FROM invoices
GROUP BY billing_id
HAVING COUNT(*) > 5;

-- DISTINCT
SELECT COUNT(DISTINCT billing_id) FROM invoices;

-- SUBSTR takes part of a text value. SUBSTR(invoice_date, 1, 7) turns 2026-10-28 into 2026-10, which lets you group by month.

-- total, count, and average invoice amount by status rounded to 2 decimal places
SELECT status, ROUND(SUM(amount), 2) AS total_invoiced, COUNT(*) AS no_of_invoice, ROUND(AVG(amount), 2) AS avg_invoice
FROM invoices
GROUP BY status;

--monthly invoicing for 2026
SELECT SUBSTR(invoice_date, 1, 7) AS month, COUNT(*) AS no_of_invoice, ROUND(SUM(amount), 2) AS total_invoiced
FROM invoices
WHERE invoice_date BETWEEN '2026-01-01' AND '2026-12-31'
GROUP BY month
ORDER BY month ASC;

-- customers having more than 5 invoices
SELECT COUNT(*) 
FROM (SELECT billing_id, COUNT(*)
				 FROM invoices
				 GROUP BY billing_id
				 HAVING COUNT(*) > 5);
				 
-- customers by segment largest first
SELECT segment, COUNT(*) AS customer
FROM crm_customers
GROUP BY segment
ORDER BY customer DESC;				

-- invoiced customers 
SELECT COUNT(DISTINCT billing_id) 
FROM invoices;