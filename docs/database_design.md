# Database Design

## Entity Relationship Diagram (ERD)

```mermaid
erDiagram
    CERTIFICATE {
        int id PK
        string student_name
        string reg_number
        string department
        string faculty
        string program
        string level
        string grad_year
        string issue_date
        string institution
        string certificate_file
        string passport_photo
        string certificate_hash UK
        string previous_hash
        int blockchain_index
        datetime uploaded_at
    }

    ADMIN {
        int id PK
        string username
        string email UK
        string password_hash
        datetime created_at
        string school_name
    }

    SUPER_ADMIN {
        int id PK
        string username
        string email UK
        string password_hash
        datetime created_at
    }

    ADMIN ||--o{ CERTIFICATE : "manages (via institution name)"
    SUPER_ADMIN ||--o{ ADMIN : "manages accounts"
```

**Note:** The relationship between `ADMIN` and `CERTIFICATE` is logical, based on the `institution` field in `CERTIFICATE` matching the `school_name` field in `ADMIN`. There is no strict foreign key constraint in the current schema.
