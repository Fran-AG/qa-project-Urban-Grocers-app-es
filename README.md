# Urban Grocers — API Test Suite
### Automated API testing for kit creation endpoints | Python · Pytest · Requests

---

## 📋 Overview

This project contains an automated test suite designed to validate the **kit creation endpoint** of the Urban Grocers API. Tests cover both positive and negative scenarios, ensuring the endpoint handles valid inputs correctly and rejects invalid ones with the appropriate HTTP responses.

---

## 🗂️ Project Structure

```
├── configuration.py          # Base URL and endpoint configuration
├── data.py                   # Test data and input variables
├── sender_stand_request.py   # HTTP request handler (reusable functions)
├── create_kit_name_kit_test.py  # Test cases (positive & negative)
├── .gitignore
└── README.md
```

---

## ✅ Test Coverage

| Scenario | Type |
|---|---|
| Valid kit name within character limit | Positive |
| Kit name at minimum boundary (1 char) | Positive |
| Kit name at maximum boundary | Positive |
| Empty kit name | Negative |
| Kit name exceeds character limit | Negative |
| Invalid data type (non-string) | Negative |
| Missing required field | Negative |

---

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| Python 3 | Core language |
| Pytest | Test execution and reporting |
| Requests | HTTP request handling |
| Token Authentication | API authorization |

---

## ⚙️ Key Techniques

- **Boundary value analysis** applied to kit name field validation
- **Token-based authentication** on all requests
- **HTTP status code validation** (200, 400, etc.)
- **Reusable request functions** to reduce code duplication
- **Positive and negative assertions** structured for clear failure reporting

---

## 🚀 Getting Started

### Prerequisites
- Python 3.x installed
- Dependencies installed:
```bash
pip install pytest requests
```

### Running the tests
```bash
pytest create_kit_name_kit_test.py -v
```

---

## 📄 API Documentation

Full API reference for Urban Grocers:
[View API Docs](https://cnt-7ec7c27c-1ca5-4abc-9394-c726939a70ad.containerhub.tripleten-services.com/docs/)

---

## 👤 Author

**Francisco Aguilar Garcia** — QA Engineer  
[LinkedIn](https://www.linkedin.com/in/tu-perfil) · [GitHub](https://github.com/Fran-AG) · [Portfolio](https://tu-portfolio.notion.site)
