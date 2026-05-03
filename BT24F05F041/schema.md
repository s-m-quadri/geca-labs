# Database Schema: Student Club Events and Registrations

## Entities

1. **Students**
   - Attributes: student_id (PK), name, email, year
   - Description: Represents students who can register for events.

2. **Clubs**
   - Attributes: club_id (PK), name, description, faculty_advisor
   - Description: Represents student clubs that organize events.

3. **Events**
   - Attributes: event_id (PK), club_id (FK), name, description, event_date, capacity, location
   - Description: Represents events organized by clubs with limited capacity.

4. **Registrations**
   - Attributes: registration_id (PK), student_id (FK), event_id (FK), registration_time, status
   - Description: Represents student registrations for events, with status 'registered' or 'waitlist'.

## Relationships

- **Clubs organize Events**: One club can organize many events (1:N)
- **Events have Registrations**: One event can have many registrations (1:N)
- **Students make Registrations**: One student can make many registrations (1:N)
- **Registrations link Students and Events**: Many-to-many relationship between students and events via registrations.

## Cardinality

- Clubs : Events = 1 : N
- Events : Registrations = 1 : N
- Students : Registrations = 1 : N
- Students : Events = M : N (via Registrations)

## Foreign Key Chains

- Clubs → Events → Registrations (chain of foreign keys)

## Diagram (Textual)

```
Clubs (1) ---- (N) Events (1) ---- (N) Registrations (N) ---- (1) Students
```

Note: The M:N between Students and Events is resolved via the junction table Registrations.