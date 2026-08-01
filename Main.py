def main():
    employees = {}

    while True:
        print("\n--- Simple Employee Management System ---\n"
              "1. Add Employee\n"
              "2. View All Employees\n"
              "3. View Productivity Report\n"
              "4. Exit\n")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("\nError: Enter a number")
            continue

        if choice == 1:
            emp_id = input("Employee ID: ")
            if emp_id in employees:
                print("Error: Employee ID already exists")
                continue

            emp_name = input("Name: ")
            emp_role = input("Role: ")

            try:
                emp_hours_worked = float(input("Hours Worked: "))
                emp_tasks_completed = int(input("Tasks Completed: "))
            except ValueError:
                print("\nError: Hours Worked must be an number and tasks an integer")
                continue

            auth = input("\nWrite 'continue' to add employee: ").strip().lower()
            if auth == "continue":
                employees[emp_id] = {
                    "name": emp_name,
                    "role": emp_role,
                    "hours_worked": emp_hours_worked,
                    "tasks_completed": emp_tasks_completed
                }
            else:
                print("\nAction Cancelled. Employee not added.")
                continue

            print(f"\nEmployee '{emp_name}' added successfully.")
        elif choice == 2:
            if not employees:
                print("\nError: No employees found in the database")
                continue

            print("\nID      | Name                | Role                | Hours | Tasks")
            print("-" * 65)
            for emp_id, info in employees.items():
                print(
                f"{emp_id:<7} | {info['name']:<19} | {info['role']:<19} | {info['hours_worked']:<5} | {info['tasks_completed']}")
        elif choice == 3:
            if not employees:
                print("\nError: No employees found in the database")
                continue

            print("\nProductivity Report (Tasks per Hour):")
            print("ID      | Name                | Ratio    | Status")
            print("-" * 55)
            for emp_id, info in employees.items():
                hours = info["hours_worked"]
                tasks = info["tasks_completed"]

                if hours <= 0:
                    ratio = 0.0
                    status = "No hours logged"
                else:
                    ratio = tasks / hours
                    if ratio >= 2.0:
                        status = "High"
                    elif ratio >= 1.0:
                        status = "Moderate"
                    else:
                        status = "Low"

                print(f"{emp_id:<7} | {info['name']:<19} | {ratio:<8.2f} | {status}")
        elif choice == 4:
            break

if __name__ == "__main__":
    main()