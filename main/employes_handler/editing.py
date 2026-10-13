def emp_list(employees):
    if not employees:
        print("\nEmployees not found.")
        input("press any key to continue...")
        return
    else:
        print(f"\n{'ID':<15}{'Name':<15}{'Role':<15}{'Hours':<8}{'Tasks':<6}")
        for emp in employees.values():
            print(f"{emp['ID']:<15}{emp['name']:<15}{emp['role']:<15}{emp['hours']:<8}{emp['tasks']:<6}")
        input("\nPress enter to continue...")
