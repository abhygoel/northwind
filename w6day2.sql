SELECT invoice_id, amount
FROM invoices
ORDER BY amount DESC
LIMIT 10;

-- Meant: Distributors in Pune or Mumbai
WHERE segment = 'Distributor' AND (city = 'Pune' OR city = 'Mumbai')

WHERE city IN ('Pune', 'Mumbai', 'Delhi')

WHERE email Like '%@northwind.com'. -- ends with @northwind.com
WHERE name LIKE 'R%' -- starts with R

WHERE amount BETWEEN 50000 AND 100000

WHERE invoice_date >= '2026-07-01'

-- NOT reverses NOT IN, NOT LIKE, IS NOT NULL

-- ten largest invoices
SELECT invoice_id, billing_id, amount, status
FROM invoices
ORDER BY amount DESC
LIMIT 10;

-- no of distributors in Pune, Mumbai, or Delhi
SELECT COUNT(*)
FROM crm_customers
WHERE segment = 'Distributor' AND city IN ('Pune', 'Mumbai', 'Delhi');

-- no of distributors in Pune, Mumbai, or Delhi v2
SELECT COUNT(*)
FROM crm_customers
WHERE segment = 'Distributor' AND city = 'Pune' OR city = 'Mumbai' OR city = 'Delhi';

-- no of distributors in Pune, Mumbai, or Delhi v3
SELECT COUNT(*)
FROM crm_customers
WHERE segment = 'Distributor' AND (city = 'Pune' OR city = 'Mumbai' OR city = 'Delhi');

-- orderded by city, name distributors in Pune, Mumbai, or Delhi
SELECT name, city
FROM crm_customers
WHERE segment = 'Distributor' AND city IN ('Pune', 'Mumbai', 'Delhi')
ORDER BY city ASC, name ASC;

-- customers with @northwind.com email id
SELECT COUNT(*)
FROM crm_customers
WHERE email LIKE '%@northwind.com';

-- over due invoices
SELECT COUNT(*)
FROM invoices
WHERE status = 'unpaid' AND due_date < '2026-10-01';

--customer signed up during 2025
SELECT COUNT(*)
FROM crm_customers
WHERE created_on BETWEEN '2025-01-01' AND '2025-12-31';