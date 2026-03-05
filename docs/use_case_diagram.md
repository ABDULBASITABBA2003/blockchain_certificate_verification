# Use Case Diagram

```mermaid
usecaseDiagram
    actor "Student / Guest" as Student
    actor "School Admin" as Admin
    actor "Super Admin" as SuperAdmin

    package "Public Access" {
        usecase "Verify Certificate" as UC1
        usecase "View About/Contact" as UC2
    }

    package "School Admin Portal" {
        usecase "Login (Admin)" as UC3
        usecase "View Dashboard (Certificates)" as UC4
        usecase "Upload Certificate" as UC5
        usecase "Edit Certificate" as UC6
        usecase "Delete Certificate" as UC7
        usecase "Logout (Admin)" as UC8
    }

    package "Super Admin Portal" {
        usecase "Login (Super Admin)" as UC9
        usecase "View Dashboard (Admins)" as UC10
        usecase "Add Admin" as UC11
        usecase "Edit Admin" as UC12
        usecase "Delete Admin" as UC13
        usecase "Logout (Super Admin)" as UC14
    }

    Student --> UC1
    Student --> UC2

    Admin --> UC3
    UC3 --> UC4
    UC4 --> UC5
    UC4 --> UC6
    UC4 --> UC7
    UC4 --> UC8

    SuperAdmin --> UC9
    UC9 --> UC10
    UC10 --> UC11
    UC10 --> UC12
    UC10 --> UC13
    UC10 --> UC14
```
