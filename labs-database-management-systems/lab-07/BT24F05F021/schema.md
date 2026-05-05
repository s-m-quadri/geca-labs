Entities: Members, Books, Loans, Fines

Relationships:
One Member → Many Loans (1:N)
One Book → Many Loans (1:N)
One Loan → One Fine (1:1, optional)
Chain of foreign keys: Members → Loans → Fines

Cardinality:
Members–Loans: 1:N
Books–Loans: 1:N
Loans–Fines: 1:1