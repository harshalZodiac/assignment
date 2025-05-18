
# 🧪 Finacplus Test Framework

This is a unified test automation framework built using Python. It supports both **API testing** and **UI testing**. You can run any test case using a single, consistent setup — ideal for teams aiming for simplicity and scalability.

---

## 📁 Project Structure

```
Finacplus/
├── api_services/       # API payloads and endpoints
├── api_tests/          # API test cases
├── config/             # Configuration files
├── page_objects/       # Page Object Model for UI tests
├── ui_tests/           # UI test cases
├── utilities/          # Common utilities and helpers
├── settings.py         # Global settings
├── conftest.py         # Pytest fixtures
├── requirements.txt    # Python dependencies
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone <your-repo-url>
cd Finacplus
```

### 2. Create and Activate Virtual Environment

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🚀 How to Run Tests

### ✅ Run All API Tests

```bash
pytest api_tests/
```

### ✅ Run All UI Tests

```bash
pytest ui_tests/
```

### ✅ Run a Specific Test Case (API or UI)

```bash
pytest <path_to_test_file>::<test_function_name>
```

Example:

```bash
pytest api_tests/test_login_api.py::test_valid_login
```

---

## 🛠 Tools & Tech

- **Language**: Python
- **Test Runner**: Pytest
- **UI Automation**: Selenium (via `page_objects`)
- **API Testing**: Requests
- **Config Management**: Custom settings via `settings.py` and `config/`

---

## 🤝 Contributing

To contribute, fork the repository and submit a pull request with clear comments and test coverage.

