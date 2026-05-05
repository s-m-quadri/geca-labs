# Project Report: Library Management System
**Author:** Anant Joshi (PRN: BT24F05F068)

## Problem Statement
Libraries need an efficient way to organize books by category and track borrowing activities. This system helps manage book records and their classifications.

## Design Decisions
- **Normalization**: Categories are separated to avoid redundancy (3NF).
- **View Usage**: `v_book_directory` provides a simplified listing of books with categories.

## Sample Results
| Category | Book Count | Avg Title Length |
| :--- | :--- | :--- |
| Technology | 2 | 20.50 |
| Fiction | 1 | 13.00 |

## Limitations and Future Scope
- No return tracking system
- Future: Add fine calculation and due dates

## References
- MySQL Documentation for AUTO_INCREMENT and JOIN syntax.
- Lab 7 instruction manual.