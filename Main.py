import string
import sys
import random

employees = {}

def id_generator(min, max):
    while True:
        emp_id = f"EMP-{random.randint(min, max)}" #-- generates an random string of nubmers from m
        if emp_id not in employees: #-- checks if generated id is not taken and in case it is returns unique generated "worker_id"
            return worker_id

def new_emp():
    emp_id = input("\nID: ")

    if not emp_id: #-- Return "True" when "emp_id" is empty
        print("\nError: ID cannot be empty.")
        return
    elif emp_id in employees: #-- Return "True" when "emp_id"
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
            employees[worker_id] = {"ID" : emp_id,
                "name" : name,
                "role" : role,
                "hours" : hours_str,
                "tasks" : tasks_str
            }
            print(f"\nEmployee {worker_id} has been added.")
            break
        elif confirm == "n":
            print("\nEmployee creation cancelled.")
            break
        else:
            print("\nError: Invalid input.")
            continue

def edit_emp():
    for emp_id in employees: #-- prints all employees Ids and their name
        print(f"\nID: {emp_id}\n | Name: {employees[emp_id]['name']}")

    emp_id = (input("\nID: ")).strip()
    if emp_id not in employees: #-- Return "True" when emp_id does not registred in employees
        print("\nError: ID does not exist.")
        return
    elif not emp_id: #-- Return "True" when "emp_id" is empty
        print("\nError: ID cannot be empty.")
        return

    emp = employees[worker_id] # -- declares that "emp" is an employee with an specific Id, the same id that user selected

    print("\nEmployee Details:\n"
        f"ID: {worker_id}\n"
        f"Name: {emp['name']}\n"
        f"Role: {emp['role']}\n"
        f"Hours: {emp['hours_str']}\n"
        f"Tasks: {emp['tasks_str']}\n"
    )

    while True:
        print(
            "\nSelect an option\n"
            "1. Change name\n"
            "2. Change role\n"
            "3. change hours\n"
            "4. change tasks\n"
            "e. exit\n"
        )

        select = input("").strip().lower()
        if select == "1": # -- Change name
            new_name = input("\nName: ").strip()
            if not new_name: #-- Return "True" when "new_name" is empty
                print("\nError: Name cannot be empty.")
                continue

            confirm = input("\nConfirm? (y/n): ").strip().lower()
            if confirm in ("y", "yes"): #-- Return "True" when confirm = y or confirm = yes but in more nice and easier to manage way
                employees[worker_id]["name"] = new_name
                print(f"\nEmployee {worker_id} name has been succsesfully changed to {new_name}.")
                continue
            else:
                print("\nError: Action cancelled.")
                continue

        elif select == "2": # -- Change role
            new_role = input("\nRole: ").strip()
            if not new_role: #-- Return "True" when "new_role" is empty
                print("\nError: Role cannot be empty.")
                continue

            confirm = input("\nConfirm? (y/n): ").strip().lower()
            if confirm in ("y", "yes"): #-- Return "True" when confirm = y or confirm = yes but in more nice and easier to manage way
                employees[worker_id]["role"] = new_role
                print(f"\nEmployee {worker_id} role has been succsesfully changed to {new_role}.")
                continue
            else:
                print("\nError: Action cancelled.")
                continue

        elif select == "3": #-- change emp hours
            while True:
                emp = employees[worker_id] # -- declares that "emp" is an employee with an specific Id, the same id that user selected

                print(
                    "\nSelect an option\n"
                    "1. Add hours\n"
                    "2. Substract hours\n"
                    "3. set hours\n"
                    "e. exit\n"
                )

                choice = input("").strip().lower()
                if choice == "1": #-- Add hours
                    amount = int(input("\nAmount: ")).strip()
                    confirm = input("\nConfirm? (y/n): ").strip().lower()
                    if confirm in ("y", "yes"): employees[worker_id]["hours"] += amount
                    else:
                        print("\nError: Action cancelled.")
                        continue
                elif choice == "2": #-- Substract hours
                    amount = int(input("\nAmount: ")).strip()
                    confirm = input("\nConfirm? (y/n): ").strip().lower()
                    if confirm in ("y", "yes"): employees[worker_id]["hours"] -= amount
                    else:
                        print("\nError: Action cancelled.")
                        continue
                elif choice == "3": #-- Set hours
                    pass
                elif choice == "e": #-- exit
                    break
                else:
                    print("\nError: invalid input.")
            continue

        elif select == "4": #-- change emp tasks
            pass

        elif select == "e": # -- exit
            print("\nEmployee Details:\n"
                  f"ID: {worker_id}\n"
                  f"Name: {emp['name']}\n"
                  f"Role: {emp['role']}\n"
                  f"Hours: {emp['hours_str']}\n"
                  f"Tasks: {emp['tasks_str']}\n"
                  )
            break

        else:
            print("\nError: Invalid input.")
            continue

def list_emps():
    print(f"\n{'ID':<6}{'Name':<15}{'Role':<15}{'Hours':<8}{'Tasks':<6}")
    for w_id, emp in employees.items(): #-- prints employees in nice way.
        print(f"{w_id:<6}{emp['name']:<15}{emp['role']:<15}{emp['hours']:<8}{emp['tasks']:<6}")
