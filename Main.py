def main():
    employees = {}

    while True:
        print("\n--- Employee Management System ---\n"
              "1. Add Employee\n"
              "2. View All Employees\n"
              "3. View Productivity Report\n"
              "4. Exit\n")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            emp_id = input("Employee ID: ")
            if emp_id in employees:
                print("Error: Employee ID already exists")
                continue

            emp_name = input("Name: ")
            emp_role = input("Role: ")

            try:
                emp_hours_worked = float(input("Hours Worked: "))
                emp_tasks_completed = int(input("Tasts Completed: "))
            except ValueError:
                print("Error: Hours Worked must be an number and tasks an integer")

            employees[emp_id] = {
                "name": emp_name,
                "role": emp_role,
                "hours_worked": emp_hours_worked,
                "tasks_completed": emp_tasks_completed
            }

            print(f"Employee '{emp_name}' added successfully.")

        elif choice == 2:
            if not employees:
                print("\nError: No employees found in the database")
                continue

        print("\nID      | Name                | Role                | Hours | Tasks")
        print("-" * 65)
        for emp_id, info in employees.items():
            print(
                f"{emp_id:<7} | {info['name']:<19} | {info['role']:<19} | {info['hours_worked']:<5} | {info['tasks_completed']}")

if __name__ == "__main__":
    main()