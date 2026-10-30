SELECT name, email, city
FROM crm_customers;

SELECT name, email
FROM crm_customers
WHERE city = 'Pune';

SELECT invoice_id, amount
FROM invoices
WHERE amount > 200000;

SELECT * FROM invoices LIMIT 5;

SELECT COUNT(*) FROM crm_customers WHERE city = 'Mumbai';