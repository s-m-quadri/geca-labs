# Library Management System Schema

## Entities

### 1. Member
Stores library user details.

### 2. Author
Stores author information.

### 3. Category
Stores book categories.

### 4. Book
Stores all book information.

### 5. Borrow
Stores borrowing transactions.

### 6. Fine
Stores penalty records.

## Relationships

- One Member can borrow many Books.
- One Book belongs to one Author.
- One Book belongs to one Category.
- One Borrow record may generate one Fine.

## Advanced Features

- Input validation using CHECK constraints
- Faster search using indexes
- Automatic inventory update using trigger