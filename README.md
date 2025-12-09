# Python Playwright Test Framework

A modern, maintainable end-to-end testing framework using Python, Playwright, and pytest with Page Object Model (POM) design pattern.

## 🚀 Features

- **Page Object Model (POM)**: Clean, maintainable test architecture
- **Playwright**: Fast, reliable cross-browser automation
- **pytest**: Powerful testing framework with extensive plugin ecosystem
- **Environment Configuration**: Secure configuration management with `.env` files
- **HTML Reports**: Detailed test execution reports
- **Parallel Execution**: Run tests faster with pytest-xdist
- **UV Package Manager**: Lightning-fast dependency management

## 📋 Prerequisites

- Python 3.9 or higher
- [uv](https://github.com/astral-sh/uv) package manager

### Install UV

```bash
# macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Or with Homebrew
brew install uv
```

## 🛠️ Setup

### 1. Clone the Repository

```bash
git clone py-test-framework
cd py-test-framework
```

### 2. Install Dependencies

```bash
# Install all dependencies
uv sync

# Install Playwright browsers
uv run playwright install
```

### 3. Configure Environment Variables

Create a `.env` file in the project root:

Add your configuration to `.env`:

```env
WEB_URL=https://qa-practice.netlify.app/bugs-form
```

## 📁 Project Structure

```
py-test-framework/
├── tests/
│   ├── pages/                  # Page Object Models
│   │   ├── __init__.py
│   │   ├── base_page.py       # Base page class
│   │   └── registration_page.py # Registration page objects
│   ├── test_first_name.py     # First name field tests
│   ├── test_last_name.py      # Last name field tests
│   └── test_registration.py   # Registration flow tests
├── .env                        # Environment variables (git-ignored)
├── .gitignore                  # Git ignore rules
├── pyproject.toml              # Project configuration & dependencies
├── README.md                   # This file
└── report.html                 # Test execution report (generated)
```

## 🧪 Running Tests

### Run All Tests

Describing the steps to run via UV but can use make file commands as well

```bash
uv run test
```

### Run Tests with Headed Browser (visible)

```bash
uv run test:headed
```

### Run Specific Test File

```bash
uv run pytest tests/test_registration.py
```

### Run Specific Test Function

```bash
uv run pytest tests/test_registration.py::test_register_user_with_all_data
```

### Run Tests with Specific Browser

```bash
uv run pytest --browser chromium
uv run pytest --browser firefox
uv run pytest --browser webkit
```

### Run Tests in Parallel

```bash
uv run pytest tests/ -n auto
```

### Generate HTML Report

```bash
uv run pytest tests/ --html=report.html --self-contained-html
```

## 🎯 Available Scripts

Defined in `pyproject.toml` under `[tool.uv.scripts]`:

| Command               | Description                      |
| --------------------- | -------------------------------- |
| `uv run test`         | Run all tests                    |
| `uv run test:headed`  | Run tests with visible browser   |
| `uv run test:codegen` | Launch Playwright code generator |
| `uv run test:install` | Install Playwright browsers      |

## 📝 Writing Tests

### Example Test Using POM

```python
import os
from dotenv import load_dotenv
from pages.registration_page import RegistrationPage

load_dotenv()

def test_register_user(page):
    web_url = os.getenv('WEB_URL')

    registration_page = RegistrationPage(page)
    registration_page.goto(web_url)

    # Method chaining for cleaner test code
    registration_page \
        .fill_first_name("John") \
        .fill_last_name("Doe") \
        .fill_phone("1234567890") \
        .select_country("USA") \
        .fill_email("john@example.com") \
        .fill_password("password123") \
        .click_register()

    # Assertions
    assert registration_page.is_success_message_visible()
```

## 🎨 Code Generation

Generate new test code using Playwright's codegen tool:

```bash
# Start codegen with your target URL
uv run test:codegen https://qa-practice.netlify.app/bugs-form

# Generate tests for specific browser
uv run playwright codegen --browser firefox https://example.com
```

## 🔍 Debugging Tests

### Run with Debug Mode

```bash
# Interactive debugging
uv run pytest tests/test_registration.py --headed --slowmo 1000

# With Playwright Inspector
PWDEBUG=1 uv run pytest tests/test_registration.py
```

### View Test Traces

Traces are automatically saved on failure. To view:

```bash
uv run playwright show-trace test-results/<trace-file>.zip
```

## 📊 Test Reports

After test execution, view the HTML report:

```bash
open report.html  # macOS
```

Reports include:

- Test execution summary
- Pass/fail status for each test
- Screenshots on failures
- Execution time
- Browser information

## 🤝 Contributing

1. Create a new branch for your feature
2. Follow POM pattern for new pages
3. Write descriptive test names
4. Add appropriate assertions
5. Update README if needed

## 📚 Additional Resources

- [Playwright Python Docs](https://playwright.dev/python/)
- [pytest Documentation](https://docs.pytest.org/)
- [UV Documentation](https://github.com/astral-sh/uv)

## ⚙️ CI/CD Integration

### GitHub Actions Example

```yml
name: Playwright Tests
on:
  workflow_dispatch:

jobs:
  test:
    timeout-minutes: 10
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v6

      - name: Install uv
        uses: astral-sh/setup-uv@v4
        with:
          enable-cache: true
          cache-dependency-glob: "uv.lock"

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version-file: "pyproject.toml" # Reads version from your config

      - name: Install dependencies
        run: uv sync --all-extras --dev

      - name: Install Playwright browsers
        run: uv run playwright install --with-deps

      - name: Run Playwright tests
        run: uv run pytest
    
      - uses: actions/upload-artifact@v5
        if: ${{ !cancelled() }}
        with:
          name: playwright-traces
          path: test-results/
```

## 📄 License

MIT License

## 👥 Authors

Gurjeet Bains
