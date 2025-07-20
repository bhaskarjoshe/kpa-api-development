# KPA API Development Assignment

## Assignment Overview
This project is a backend API implementation for the KPA Form Data system, developed as part of the backend assignment. The goal is to implement at least two fully functional APIs as specified in the provided Postman collection and SwaggerHub documentation, using Django REST Framework and PostgreSQL.

---

## Tech Stack
- **Backend Framework:** Django 5.2.4, Django REST Framework
- **Database:** PostgreSQL
- **Python Version:** 3.10+
- **Environment Variables:** Managed via `.env` file (see below)

---

## Implemented APIs
###  1. Wheel Specification List & Create
- **Endpoint:** `/api/form_data/wheel-specifications`
- **Methods:**
  - `GET`: List all wheel specifications
  - `POST`: Create a new wheel specification
- **Request Body (POST):**
  ```json
  {
    "formNumber": "string",
    "submittedBy": "string",
    "submittedDate": "YYYY-MM-DD",
    "fields": { ... } // JSON object with form fields
  }
  ```
- **Example:**
    ```json
    {
        "formNumber": "WHEEL-2025-003",
        "submittedBy": "user_id_789",
        "submittedDate": "2025-07-15",
        "fields": {
            "treadDiameterNew": "910 (895-1005)",
            "lastShopIssueSize": "835 (805-895)",
            "condemningDia": "820 (800-880)",
            "wheelGauge": "1601 (+1.5,-0.5)",
            "variationSameAxle": "0.6",
            "variationSameBogie": "5.2",
            "variationSameCoach": "14",
            "wheelProfile": "29.2 Flange Thickness",
            "intermediateWWP": "19 TO 27",
            "bearingSeatDiameter": "130.045 TO 130.067",
            "rollerBearingOuterDia": "280 (+0.002/-0.034)",
            "rollerBearingBoreDia": "130 (+0.001/-0.024)",
            "rollerBearingWidth": "93 (+0/-0.210)",
            "axleBoxHousingBoreDia": "280 (+0.031/+0.051)",
            "wheelDiscWidth": "127 (+5/-0)"
        }
    }
    ```

- **Response (201 Created):**
  ```json
  {
    "id": 1,
    "formNumber": "...",
    "submittedBy": "...",
    "submittedDate": "...",
    "fields": { ... }
  }
  ```
- **Response (GET):**
  ```json
  [
    {
      "id": 1,
      "formNumber": "...",
      "submittedBy": "...",
      "submittedDate": "...",
      "fields": { ... }
    },
    ...
  ]
  ```

---

### 2. Bogie Checksheet List & Create
- **Endpoint:** `/api/form_data/bogie-checksheets`
- **Methods:**
  - `GET`: List all bogie checksheets
  - `POST`: Create a new bogie checksheet
- **Request Body (POST):**
  ```json
  {
    "formNumber": "string",
    "inspectionBy": "string",
    "inspectionDate": "YYYY-MM-DD",
    "bogieDetails": { ... },
    "bogieChecksheet": { ... },
    "bmbcChecksheet": { ... },
    "status": "Saved"
  }
  ```
- **Example:**
    ```json
    {
      "formNumber": "BOGIE-2025-001",
      "inspectionBy": "user_id_456",
      "inspectionDate": "2025-07-03",
      "bogieDetails": {
        "bogieNo": "BG1234",
        "makerYearBuilt": "RDSO/2018",
        "incomingDivAndDate": "NR / 2025-06-25",
        "deficitComponents": "None",
        "dateOfIOH": "2025-07-01"
      },
      "bogieChecksheet": {
        "bogieFrameCondition": "Good",
        "bolster": "Good",
        "bolsterSuspensionBracket": "Cracked",
        "lowerSpringSeat": "Good",
        "axleGuide": "Worn"
      },
      "bmbcChecksheet": {
        "cylinderBody": "WORN OUT",
        "pistonTrunnion": "GOOD",
        "adjustingTube": "DAMAGED",
        "plungerSpring": "GOOD"
      }
  }
    ```

- **Response (201 Created):**
  ```json
  {
    "id": 1,
    "formNumber": "...",
    "inspectionBy": "...",
    "inspectionDate": "...",
    "bogieDetails": { ... },
    "bogieChecksheet": { ... },
    "bmbcChecksheet": { ... },
    "status": "Saved"
  }
  ```

---

## Project Setup Instructions

### 1. Clone the Repository
```bash
git clone <your-repo-url>
cd KPA-API-Development
```

### 2. Create and Activate Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables
Create a `.env` file in the project root with the following content:
```
DB_NAME=<your_db_name>
DB_USER=<your_db_user>
DB_PASSWORD=<your_db_password>
DB_HOST=localhost
DB_PORT=5432
```

### 5. Apply Migrations
```bash
python manage.py migrate
```

### 6. Run the Development Server
```bash
python manage.py runserver
```

---

## Testing the APIs
- Use the provided Postman collection (`KPA_form data.postman_collection.json`) to test the implemented endpoints.
- Example login credentials (if authentication is required):
  - **Phone Number:** `7760873976`
  - **Password:** `to_share@123`
- Ensure the PostgreSQL database is running and accessible.

---

## References & Resources
- [Hosted API Reference](https://kpa.suvidhaen.com)
- [Frontend Code](https://github.com/s2pl/KPA-ERP-FE/)
- [API Documentation (SwaggerHub)](https://app.swaggerhub.com/apis/sarvasuvidhaen/kpa-form_data/1.0.0)

---

### Authentication
- Some endpoints may require authentication.
- Example credentials:
  - **Phone Number:** `7760873976`
  - **Password:** `to_share@123`
- If authentication is required, obtain a token via the login endpoint (document the endpoint if implemented).

### Error Handling
- Errors are returned in standard DRF format:
  ```json
  {
    "detail": "Error message here."
  }
  ```