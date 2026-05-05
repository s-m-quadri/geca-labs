# Library Management System - Report

## Problem
This system manages book borrowing in a library.

## Design
We created 4 tables:
- Members
- Books
- Staff
- Borrow (relationship table)

Normalization is applied to avoid redundancy.

## Features
- Track borrowed books
- Identify active users
- Monitor staff activity

## Sample Queries
- Most active member
- Books not returned
- Total books borrowed

## Limitations
- No login system
- No fine calculation

## Future Scope
- Add penalties
- Add reservation system