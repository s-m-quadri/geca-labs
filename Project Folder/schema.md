# Schema Design

Entities:
- Student
- Company
- Application
- Interview

Relationships:
- Student ↔ Company is M:N (via Application)
- One Application → many Interview rounds (1:N)

Chain:
Student → Application → Interview

Normalization:
- Removed repeated company/student data
- Used junction table for M:N relationship

Constraints:
- CASCADE delete ensures cleanup of applications/interviews