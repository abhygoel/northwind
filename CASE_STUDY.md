# Cleaning and deduplicating a 5,000-customer CRM export

*Client: Northwind Supplies (fictional), a distributor with customers across 10 Indian cities*

## The problem

Northwind's sales team had stopped trusting their customer list. Names, emails and phone numbers were typed in many different ways, some records were incomplete or simply wrong, and the same customer often appeared more than once. That meant duplicate calls, duplicate invoices, and reports nobody could rely on.

The proper fix, changing how every rep enters data, would take months. Northwind needed a dependable way to clean the list they already had, and to repeat it every week.

## What I built

A single command that takes the CRM export and produces five files the team can act on:

| File | Purpose |
|---|---|
| Clean customer list | Valid customers, consistently formatted, each one exactly once |
| Fix list | Invalid records, shown exactly as they appear in the CRM, with the reason for each |
| Removed duplicates | Every record taken out, with the record it duplicated |
| Review list | Possible duplicates for a person to decide on, with the evidence |
| Summary | A short report, ready to paste into an email |

The original export is never changed, so every result can be traced back to its source.

## Results

- **5,000 records** sorted into 3,737 clean, 963 to fix, and 300 duplicates removed.
- **201 spellings of city names** turned out to be 10 cities. Without cleaning, a "customers by city" report would have been wrong for every city.
- **Half the duplicates were hidden.** 150 were visible as exact copies; another 150 only appeared once formatting was made consistent, for example `+91 98765 43210` and `9876543210`.
- **200 possible duplicates sent to a person** instead of being guessed at.
- **Bad records that looked fine:** on an earlier 300-record export, tightening the rules found 36 invalid records that the original checks had passed as clean.
- **Fast and safe to rerun:** the full file is processed in under a tenth of a second, and 39 automated tests confirm every rule still works after any change.

## Decisions and trade-offs

Deleting a record is easy to do and hard to undo, so the tool only removes what it can prove is a duplicate: records that are identical once formatting is fixed. Every removal is logged alongside the record it copied, so nothing disappears without a trace.

Everything less certain goes to a person, labelled by the strength of the evidence:

- **Same email address:** "likely same person". For example, *Lakshmi Sheikh* and *L. Sheikh* share an email and a phone number.
- **Same phone number only:** "check before merging". Families often share a number, as with *Neha Nair* and *Anil Nair*, and merging them would lose a real customer.

Rules can't catch everything. One customer, *Arjun Patel*, appears twice with the same phone but two different email addresses. That's most likely one person with work and personal emails, not two family members, and it's exactly the kind of case a person should decide.

One trap the tool deliberately avoids: 139 customers had no email at all. A naive duplicate check would have treated them as one customer and, if allowed to merge automatically, wiped out 138 real records. Blank values are never used to match records.

## What I'd do next

- **One review list per pair,** showing every reason two records match (same email, same phone, similar name) so the reviewer sees all the evidence at once.
- **Run it automatically every week** and track how data quality changes over time.
- **Fix the cause:** add validation at the point of data entry so the same mistakes stop arriving.
- **Use AI where rules struggle:** for example, judging whether "R. Kumar" and "Ravi Kumar" are the same person, with a human still approving any merge.
