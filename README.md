# AI Box Selection System

A Django REST Framework application that recommends the most cost-effective shipping box for customer orders based on product dimensions and weight.

The system automatically evaluates all available shipping boxes and selects the lowest-cost box that can safely accommodate the order.

---

# Table of Contents

- Project Overview
- Features
- System Architecture
- Technology Stack
- Project Structure
- Installation
- Configuration
- Database Setup
- Running the Application
- Running Tests
- API Documentation
- Recommendation Algorithm
- Sample API Workflow
- Business Rules
- Assumptions
- Error Handling
- Testing
- Future Improvements
- Author

---

# Project Overview

This project provides a backend service for an e-commerce shipping workflow.

When a customer places an order containing one or more products, the system:

- Calculates the total shipping weight
- Determines the required packing dimensions
- Searches all available shipping boxes
- Filters compatible boxes
- Selects the lowest-cost compatible box
- Stores the recommended shipping box with the order

The application exposes REST APIs using Django REST Framework.

---

# Features

## Product Management

- Store product dimensions
- Store product weight
- Product catalog support

## Shipping Box Management

- Store shipping box dimensions
- Store maximum supported weight
- Store shipping cost

## Order Management

- Create customer orders
- Add multiple products to an order
- Retrieve complete order details

## Recommendation Engine

Automatically:

- Calculates total order weight
- Calculates packing dimensions
- Finds compatible boxes
- Selects the cheapest compatible shipping box

## REST APIs

Complete REST API implementation using Django REST Framework.

## Automated Testing

Includes automated tests for:

- Models
- Recommendation Service
- REST APIs

---

# System Architecture

```
                   Products
                      │
                      │
                      ▼
               Order + Order Items
                      │
                      ▼
         Recommendation Service
                      │
      ┌───────────────┴───────────────┐
      │                               │
 Calculate Requirements       Find Compatible Boxes
      │                               │
      └───────────────┬───────────────┘
                      │
                      ▼
            Select Cheapest Box
                      │
                      ▼
          Save Recommendation
```

---

# Technology Stack

| Technology | Version |
|------------|----------|
| Python | 3.x |
| Django | 5.x |
| Django REST Framework | Latest |
| SQLite | Default Database |
| Git | Version Control |

---

# Project Structure

```
ai-box-selection-system/

├── apps/
│   ├── boxes/
│   ├── orders/
│   ├── products/
│   └── recommendations/
│
├── config/
│
├── manage.py
├── requirements.txt
├── README.md
├── AI_USAGE.md
└── TEST_OUTPUT.md
```

---

# Installation

Clone the repository

```bash
git clone <repository-url>
```

Move into the project

```bash
cd ai-box-selection-system
```

Create virtual environment

```bash
python -m venv .venv
```

Activate virtual environment

### Windows

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# Database Setup

Run migrations

```bash
python manage.py migrate
```

Create superuser

```bash
python manage.py createsuperuser
```

---

# Running the Application

Start the development server

```bash
python manage.py runserver
```

Application will be available at

```
http://127.0.0.1:8000/
```

Admin Panel

```
http://127.0.0.1:8000/admin/
```

---

# Running Tests

Execute all automated tests

```bash
python manage.py test
```

Example output

```
Found 10 test(s).

..........
----------------------------------------------------------------------
Ran 10 tests

OK
```

---

# API Documentation

## Create Order

**POST**

```
/api/orders/
```

Request

```json
{
    "customer_name": "John Doe"
}
```

---

## List Orders

**GET**

```
/api/orders/
```

---

## Retrieve Order

**GET**

```
/api/orders/<id>/
```

---

## Add Product to Order

**POST**

```
/api/orders/items/
```

Request

```json
{
    "order": 1,
    "product": 1,
    "quantity": 2
}
```

---

## Recommend Shipping Box

**POST**

```
/api/orders/<id>/recommend/
```

Response

```json
{
    "message": "Shipping box recommended successfully.",
    "data": {
        ...
    }
}
```

---

# Recommendation Algorithm

The recommendation process follows these steps:

1. Retrieve all products in the order.
2. Calculate the total shipping weight.
3. Calculate the required packing dimensions.
4. Retrieve all available shipping boxes.
5. Filter boxes that satisfy:

- Length requirement
- Width requirement
- Height requirement
- Maximum weight requirement

6. Sort compatible boxes by shipping cost.
7. Select the cheapest compatible shipping box.
8. Save the recommendation to the order.

If no compatible box exists, an exception is raised.

---

# Sample Workflow

1. Create Products
2. Create Shipping Boxes
3. Create an Order
4. Add Products to the Order
5. Call Recommendation API
6. Retrieve Updated Order

---

# Business Rules

- Every product has dimensions and weight.
- Every shipping box has dimensions, maximum weight, and cost.
- A shipping box must satisfy all dimension and weight constraints.
- The system always recommends the lowest-cost compatible box.
- If no compatible shipping box exists, the API returns an error.

---

# Assumptions

- Product dimensions are stored in consistent units.
- Shipping box dimensions use the same measurement units.
- Shipping costs are predefined.
- Orders may contain multiple products.
- Products are packed vertically when calculating height.

---

# Error Handling

The application handles:

- Invalid requests
- Missing resources
- Validation errors
- No compatible shipping box found

Example

```json
{
    "error": "No suitable shipping box found."
}
```

---

# Testing

The project contains automated tests for:

## Recommendation Service

- Calculate packing requirements
- Find compatible boxes
- Select cheapest box
- Handle no suitable box scenario

## Order Model

- Total weight calculation
- Packing dimensions calculation
- String representation

## API Tests

- Create Order
- List Orders
- Retrieve Order

---

# Future Improvements

Possible enhancements include:

- Authentication and authorization
- Inventory management
- Shipping provider integration
- Multiple packing strategies
- 3D bin packing optimization
- Cost estimation based on destination
- Swagger/OpenAPI documentation
- Docker support
- PostgreSQL deployment
- CI/CD pipeline

---

# Author

**Ravinder Kumar**

Backend Developer

Built using Python, Django, and Django REST Framework.