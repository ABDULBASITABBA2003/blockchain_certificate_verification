# Use Case Descriptions

## 1. Verify Certificate

| Field | Description |
| :--- | :--- |
| **Actor** | Student / Guest |
| **Description** | Allows a user to verify the authenticity of a certificate by entering a registration number or hash. |
| **Preconditions** | The system must be accessible via a web browser. The certificate must exist in the database. |
| **Post-conditions** | The user receives the certificate details if found, or a "No matching certificate found" message. |
| **Flow** | 1. User navigates to the "Verify Certificate" page.<br>2. User enters a registration number or certificate hash.<br>3. System queries the database.<br>4. System displays the result page with certificate details (valid) or an error message (invalid). |

## 2. Upload Certificate

| Field | Description |
| :--- | :--- |
| **Actor** | School Admin |
| **Description** | Allows an admin to upload a new certificate, including student details, certificate file, and passport photo. The system generates a hash and adds it to the blockchain. |
| **Preconditions** | The admin must be logged in. The student's registration number must not already exist for the institution. |
| **Post-conditions** | A new certificate record is created in the database. A new block is added to the blockchain. The certificate file and passport photo are saved to the server. |
| **Flow** | 1. Admin logs in and navigates to the "Upload Certificate" page.<br>2. Admin fills in the student details form (Name, Reg No, Dept, etc.).<br>3. Admin uploads the certificate file (PDF/Image) and passport photo.<br>4. Admin submits the form.<br>5. System validates the input and checks for duplicates.<br>6. System saves the files.<br>7. System generates a unique hash for the certificate.<br>8. System adds the certificate data to the blockchain.<br>9. System saves the certificate record to the database.<br>10. System redirects to a success page. |

## 3. Manage Admins (Add Admin)

| Field | Description |
| :--- | :--- |
| **Actor** | Super Admin |
| **Description** | Allows the Super Admin to add a new School Admin to the system. |
| **Preconditions** | The Super Admin must be logged in. The email address must not already be registered. |
| **Post-conditions** | A new admin account is created in the database. |
| **Flow** | 1. Super Admin logs in and navigates to the "Add Admin" page.<br>2. Super Admin enters the new admin's name, email, password, and school name.<br>3. Super Admin submits the form.<br>4. System checks if the email already exists.<br>5. System hashes the password and saves the new admin to the database.<br>6. System displays a success message and redirects to the dashboard. |
