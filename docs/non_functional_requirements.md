# Non-Functional Requirements

## 1. Security
- **Authentication:** The system shall use secure password hashing (PBKDF2 via Werkzeug) for storing user credentials.
- **Access Control:** The system shall enforce role-based access control (RBAC) to restrict access to sensitive functionalities (e.g., certificate uploads, admin management).
- **Session Management:** The system shall use secure, signed cookies for session management to prevent session hijacking.
- **Input Validation:** The system shall validate user inputs (e.g., registration numbers, file uploads) to prevent common web vulnerabilities like SQL injection and cross-site scripting (XSS).
- **Secure File Handling:** Uploaded files (certificates and passport photos) shall be sanitized using `secure_filename` to prevent directory traversal attacks.
- **CSRF Protection:** Forms shall be protected against Cross-Site Request Forgery (CSRF) attacks (implied by Flask usage, though not explicitly seen in snippets).

## 2. Performance & Scalability
- **Database:** The system currently uses SQLite, which is suitable for small-scale deployments but may become a bottleneck under high concurrent write loads due to locking mechanisms.
- **File Storage:** Certificates and images are stored on the local file system. This limits scalability across multiple servers. Future iterations should consider cloud storage (e.g., AWS S3).
- **Blockchain Limitations:** The current blockchain implementation relies on an in-memory structure (`blockchain/blockchain.py`) which resets upon application restart. While certificate data and hashes are persisted in the database, the chain's continuity in memory is not durable across restarts.

## 3. Reliability & Availability
- **Uptime:** The system relies on a single application server instance. High availability would require load balancing and redundant server instances.
- **Data Integrity:** Certificate hashes ensure that modifications to certificate data can be detected. However, the lack of a distributed ledger means the "blockchain" is centralized and mutable by database administrators.

## 4. Technology Stack
- **Backend Framework:** Python Flask
- **Database:** SQLite (via SQLAlchemy ORM)
- **Frontend:** HTML5, CSS3, Bootstrap, Jinja2 Templating
- **Cryptography:** SHA-256 for certificate hashing
- **Blockchain Logic:** Custom Python implementation (Linked List structure)

## 5. Deployment
- **Environment:** The application is designed to run in a Python environment (e.g., Gunicorn/Nginx or development server).
- **Dependencies:** Managed via `requirements.txt`.
