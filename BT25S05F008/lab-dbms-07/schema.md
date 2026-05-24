Entities:
- Center
- Service
- User
- Token

Relationships:
- One center has many services (1:N)
- One service generates many tokens (1:N)
- One user can take multiple tokens (1:N)

Chain:
Center → Service → Token → User

Design:
- Avoid redundancy
- Separate entities clearly
- Token is core transactional table