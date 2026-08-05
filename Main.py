import string
import sys
import random

employees = {}

def id_generator(min, max):
    while True:
        emp_id = f"EMP-{random.randint(min, max)}"
        if emp_id not in employees:
            return worker_id

def new_emp():
    emp_id = input("\nID: ")

    if not emp_id:
        print("\nError: ID cannot be empty.")
        return
    elif emp_id in employees:
        print("\nError: ID already exists.")
        return

    name = input("\nName: ")
    if not name:
        print("\nError: Name cannot be empty.")
        return

    role = input("\nRole: ")
    if not role:
        print("\nError: Role cannot be empty.")
        return

    try:
        hours_str = int(input("\nHours: "))
        tasks_str = int(input("\nTasks: "))
    except ValueError:
        print("\nError: Invalid input.")
        return

    print("\nEmployee Details:")
    print(f"ID: {worker_id}\n"
          f"Name: {name}\n"
          f"Role: {role}\n"
          f"Hours: {hours_str}\n"
          f"Tasks: {tasks_str}")

    while True:
        confirm = input("\nConfirm? (y/n): ").lower()
        if confirm == "y":
            employees[worker_id] = {"name" : name,
                "role" : role,
                "hours" : hours_str,
                "tasks" : tasks_str
            }
            print(f"\nEmployee {worker_id} has been added.")
            break
        elif confirm == "n":
            print("\nEmployee creation cancelled.")
            return
        else:
            print("\nError: Invalid input.")

def edit_emp():
    worker_id = input("\nID: ")
    if not worker_id:
        print("\nError: ID cannot be empty.")
        return


def list_emps():
    print("\n{'ID':<6}{'Name':<15}{'Role':<15}{'Hours':<8}{'Tasks':<6}")
    for w_id, emp in employees.items():
        print(f"{w_id:<6}{emp['name']:<15}{emp['role']:<15}{emp['hours']:<8}{emp['tasks']:<6}")
