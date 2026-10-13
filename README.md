# Python QA Automation Framework

[![QA Test Suite](https://github.com/BMRedwine69/python-qa-automation-framework-/actions/workflows/tests.yml/badge.svg)](https://github.com/BMRedwine69/python-qa-automation-framework-/actions/workflows/tests.yml)
![Python](https://img.shields.io/badge/Python-3.11-3776AB?logo=python&logoColor=white)
![Pytest](https://img.shields.io/badge/Pytest-8.0-0A9EDC?logo=pytest&logoColor=white)
![Playwright](https://img.shields.io/badge/Playwright-End--to--End-2EAD33?logo=playwright&logoColor=white)

An automated end-to-end (E2E) UI and backend REST API test automation framework designed for continuous integration. Built using Python, Pytest, Playwright, and Requests.

---

## Tech Stack & Tools
* **Language:** Python 3.11
* **Test Runner:** Pytest
* **UI Automation:** Playwright (Chromium)
* **API Validation:** Requests
* **CI/CD:** GitHub Actions

---

## Framework Architecture
* `.github/workflows/tests.yml` — Automated CI pipeline triggered on push/PR
* `tests/test_ui_login.py` — End-to-end browser regression tests
* `tests/test_api_users.py` — REST API endpoint status and schema tests
* `pytest.ini` — Pytest configuration and custom execution markers
* `requirements.txt` — Project dependencies

---

## Local Setup & Execution

### 1. Clone & Install
```bash
git clone [https://github.com/BMRedwine69/python-qa-automation-framework-.git](https://github.com/BMRedwine69/python-qa-automation-framework-.git)
cd python-qa-automation-framework-
pip install -r requirements.txt
playwright install chromium
