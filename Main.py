import random

employees = {}

def emp_details(emp_id):
    if emp_id not in employees:
        print("\nError: ID does not exist.")
        return
    emp = employees[emp_id]
    print("\nEmployee Details:")
    print(f"ID: {emp['ID']}\n"
          f"Name: {emp['name']}\n"
          f"Role: {emp['role']}\n"
          f"Hours: {emp['hours']}\n"
          f"Tasks: {emp['tasks']}")

def get_int():
    while True:
        try:
            amount = int(input("\nAmount: ").strip())
            if amount < 0:
                print("\nError: Amount cannot be negative.")
                continue
            else:
                return amount
        except ValueError:
            print("\nError: Invalid input.")

def get_confirm():
    confirm = input("\nConfirm? (y/n): ").strip().lower()
    if confirm in ("y", "yes"):
        return True
    elif confirm in ("n", "no"):
        return False
    else:
        print("\nError: Invalid input.")
        return None

def id_generator():
    min_val, max_val = 0, 999999999
    while True:
        emp_id = f"EMP-{random.randint(min_val, max_val)}"
        if emp_id not in employees:
            return emp_id

def emp_new():
    while True:
        unauth = id_generator()
        print(f"\nNewly Generated id: {unauth}\n")
        if get_confirm():
            emp_id = unauth
            break
        else:
            print("\nGenerating a new ID.")
            continue

    name = input("\nName: ").strip()
    if not name:
        print("\nError: Name cannot be empty.")
        return
    role = input("\nRole: ").strip()
    if not role:
        print("\nError: Role cannot be empty.")
        return

    hours_int = get_int()
    tasks_int = get_int()

    while True:
        confirm = get_confirm()
        if confirm:
            employees[emp_id] = {"ID" : emp_id,
                "name" : name,
                "role" : role,
                "hours" : hours_int,
                "tasks" : tasks_int
            }
            emp_details(emp_id)
            print(f"\nEmployee {emp_id} has been added.")
            break
        elif confirm is False:
            print("\nEmployee creation cancelled.")
            break
        else:
            continue

def emp_edit():
    for emp_id in employees:
        print(f"\nID: {emp_id}\n | Name: {employees[emp_id]['name']}")
    emp_id = input("\nID: ").strip()
    if not emp_id:
        print("\nError: ID cannot be empty.")
        return
    elif emp_id not in employees:
        print("\nError: ID does not exist.")
        return

    emp = employees[emp_id]
    emp_details(emp_id)

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
        if select == "1":
            new_name = input("\nName: ").strip()
            if not new_name:
                print("\nError: Name cannot be empty.")
                continue

            confirm = get_confirm()
            if confirm:
                emp["name"] = new_name
                print(f"\nEmployee {emp_id} name has been successfully changed to {new_name}.")
                continue
            elif confirm is False:
                print("\nError: Action cancelled.")
                continue
            else:
                continue
        elif select == "2":
            new_role = input("\nRole: ").strip()
            if not new_role:
                print("\nError: Role cannot be empty.")
                continue

            confirm = get_confirm()
            if confirm:
                emp["role"] = new_role
                print(f"\nEmployee {emp_id} role has been successfully changed to {new_role}.")
                continue
            elif confirm is False:
                print("\nError: Action cancelled.")
                continue
            else:
                continue
        elif select == "3":
            while True:
                print(
                    "\nSelect an option\n"
                    "1. Add hours\n"
                    "2. Subtract hours\n"
                    "3. set hours\n"
                    "e. exit\n"
                )

                choice = input("").strip().lower()
                if choice == "1":
                    amount = get_int()
                    confirm = get_confirm()
                    if confirm:
                        emp["hours"] += amount
                        print(f"\nEmployee {emp_id} hours has been successfully changed to {emp['hours']}.")
                    elif confirm is False:
                        print("\nError: Action cancelled.")
                        continue
                    else:
                        continue
                elif choice == "2":
                    amount = get_int()
                    confirm = get_confirm()
                    if confirm:
                        if amount > emp["hours"]:
                            emp["hours"] = 0
                            print(f"\nEmployee {emp_id} hours has been successfully changed to {emp['hours']}.")
                        else:
                            emp["hours"] -= amount
                            print(f"\nEmployee {emp_id} hours has been successfully changed to {emp['hours']}.")
                    elif confirm is False:
                        print("\nError: Action cancelled.")
                        continue
                    else:
                        continue
                elif choice == "3":
                    amount = get_int()
                    confirm = get_confirm()
                    if confirm:
                        emp["hours"] = amount
                        print(f"\nEmployee {emp_id} hours has been successfully changed to {emp['hours']}.")
                    elif confirm is False:
                        print("\nError: Action cancelled.")
                        continue
                    else:
                        continue
                elif choice == "e":
                    confirm = get_confirm()
                    if confirm:
                        print("\nExiting.")
                        emp_details(emp_id)
                        break
                    elif confirm is False:
                        print("\nError: Action cancelled.")
                        continue
                    else:
                        continue
                else:
                    print("\nError: Invalid input.")
                    continue
        elif select == "4":
            while True:
                print(
                    "\nSelect an option\n"
                    "1. Add tasks\n"
                    "2. Subtract tasks\n"
                    "3. set tasks\n"
                    "e. exit\n"
                )
                choice = input("").strip().lower()
                if choice == "1":
                    amount = get_int()
                    confirm = get_confirm()
                    if confirm:
                        emp["tasks"] += amount
                        print(f"\nEmployee {emp_id} tasks has been successfully changed to {emp['tasks']}.")
                    elif confirm is False:
                        print("\nError: Action cancelled.")
                        continue
                    else:
                        continue
                elif choice == "2":
                    amount = get_int()
                    confirm = get_confirm()
                    if confirm:
                        if amount > emp["tasks"]:
                            emp["tasks"] = 0
                            print(f"\nEmployee {emp_id} tasks has been successfully changed to {emp['tasks']}.")
                        else:
                            emp["tasks"] -= amount
                            print(f"\nEmployee {emp_id} tasks has been successfully changed to {emp['tasks']}.")
                    elif confirm is False:
                        print("\nError: Action cancelled.")
                        continue
                    else:
                        continue
                elif choice == "3":
                    amount = get_int()
                    confirm = get_confirm()
                    if confirm:
                        emp["tasks"] = amount
                        print(f"\nEmployee {emp_id} tasks has been successfully changed to {emp['tasks']}.")
                    elif confirm is False:
                        print("\nError: Action cancelled.")
                        continue
                    else:
                        continue
                elif choice == "e":
                    confirm = get_confirm()
                    if confirm:
                        print("\nExiting.")
                        emp_details(emp_id)
                        break
                    elif confirm is False:
                        print("\nError: Action cancelled.")
                        continue
                    else:
                        continue
                else:
                    print("\nError: Invalid input.")
                    continue
        elif select == "e":
            print("\nAction cancelled.")
            return
        else:
            print("\nError: Invalid input.")
            continue

def emp_list():
    if not employees:
        print("\nEmployees not found.")
        return
    else:
        print(f"\n{'ID':<15}{'Name':<15}{'Role':<15}{'Hours':<8}{'Tasks':<6}")
        for w_id, emp in employees.items():
            print(f"{emp['ID']:<15}{emp['name']:<15}{emp['role']:<15}{emp['hours']:<8}{emp['tasks']:<6}")

def main():
    pass


if __name__ == "__main__":
    main()