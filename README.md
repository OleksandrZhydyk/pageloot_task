# Project Documentation

## Project Overview

This project is a simple **Expense Tracker API**. Users can create accounts with a **username** and **email**. No authentication or authorization is required.  

The main entity is **Expense**, which has the following fields:

- `user`: The user associated with the expense
- `title`: Expense title or description
- `amount`: Expense amount (must be positive)
- `date`: Date of the expense
- `category`: Expense category (e.g., `Food`, `Travel`, `Utilities`)

---

## Prerequisites

Docker, Docker Compose must be installed.
If not, please see:

[Docker](https://docs.docker.com/engine/install/) and
[Docker compose](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-compose-on-ubuntu-22-04)
for installation instructions.

---

## Setup Instructions

**Clone the repository**

```bash
git clone <repo-url>
cd <repo-folder>
docker compose up -d
By default, the API will be available at: http://127.0.0.1:8000/
```


### API Endpoints

**Expense Endpoints**

**Create Expense**
 - URL: `/expenses/`
 - Method: POST

Body:

```json
{
  "title": "Lunch",
  "amount": 12.50,
  "date": "2025-10-22",
  "category": "FOOD",
  "user": 1
}
```


Response: Created expense object.

**Retrieve Expense**

 - URL: `/expenses/{id}/`
 - Method: GET
 - Response: Expense object with the given ID.

**Update Expense**

 - URL: `/expenses/{id}/`
 - Method: PUT or PATCH
 - Body: Updated expense fields
 - Response: Updated expense object.

**Delete Expense**

 - URL: `/expenses/{id}/`
 - Method: DELETE
 - Response: Success message or status code.

**List Expenses by Date Range**
 - URL: `/expenses/by-range/<int:user_id>`
 - Method: GET

Query Parameters:

```ini
date_range_after=YYYY-MM-DD
date_range_before=YYYY-MM-DD
```

Response: List of expenses for the user within the specified date range.

**Category Summary (Monthly)**
 - URL: `/expenses/by-category/<int:user_id>`
 - Method: GET

Query Parameters:

```ini
month=MM
?year=YYYY
```
Response: Total expenses per category for the given month:

```json
[
    {
        "category": "Food",
        "cat_expenses": 65.0
    },
    {
        "category": "Travel",
        "cat_expenses": 105.0
    },
    {
        "category": "Utilities",
        "cat_expenses": 127.0
    }
]
```