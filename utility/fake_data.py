import json
import os
import random
from faker import Faker
from datetime import datetime

fake = Faker()
DATA_DIR = "test_data"
ALL_USERS_FILE = os.path.join(DATA_DIR, "all_employees.json")


def generate_unique_employee_id(existing_ids):
    """Generate a unique 4-digit employee ID."""
    while True:
        emp_id = random.randint(1000, 9999)
        if emp_id not in existing_ids:
            return emp_id


def generate_employee_data():
    """Generate a new fake employee and save to the all_employees.json list."""
    os.makedirs(DATA_DIR, exist_ok=True)

    # Load existing users if available
    if os.path.exists(ALL_USERS_FILE):
        with open(ALL_USERS_FILE, "r") as f:
            employees = json.load(f)
    else:
        employees = []

    existing_ids = {emp.get("employee_id") for emp in employees}

    employee = {
        "employee_id": generate_unique_employee_id(existing_ids),
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "created_at": datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }

    employees.append(employee)

    with open(ALL_USERS_FILE, "w") as f:
        json.dump(employees, f, indent=4)

    return employee


def get_all_employees():
    """Return all stored employees."""
    if os.path.exists(ALL_USERS_FILE):
        with open(ALL_USERS_FILE, "r") as f:
            return json.load(f)
    return []


def get_latest_employee():
    """Return the last created employee."""
    employees = get_all_employees()
    return employees[-1] if employees else None


def get_employee_by_id(emp_id):
    """Return employee matching the given 4-digit employee_id."""
    employees = get_all_employees()
    for emp in employees:
        if emp.get("employee_id") == emp_id:
            return emp
    return None
