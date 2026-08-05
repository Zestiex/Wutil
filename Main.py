"""
class Employee:
    def __init__(self, id, name, role, hours_worked, tasks_completed):
        self.id = id
        self.name = name
        self.role = role
        self.hours_worked = hours_worked
        self.tasks_completed = tasks_completed

    def positive_float(self, promt):
        while True:
            try:
                val = float(input(promt))
                if val < 0:
                    print("\nError: Amount cannot be negative.")
                    continue
                return val
            except ValueError:
                print("\nError: Pleace enter a valid number.")

    def raw_productivity(self):
        if self.hours_worked <= 0:
            return 0.0
        return self.tasks_completed / self.hours_worked

    def clean_productivity(self):
        if self.hours_worked <= 0:
            return "No hours logged"

        ratio = self.raw_productivity()

        if ratio >= 2.0:
            return "High"
        elif ratio >= 1.0:
            return "Moderate"
        else:
            return "Low"

    def productivity(self, employees_list):
        if not employees_list:
            print("\nNo employees to display productivity for.")
            return

        id_w, name_w, ratio_w, status_w = self.calc_width(employees_list)

        header = (
            f"{'ID':<{id_w}} | "
            f"{'Name':<{name_w}} | "
            f"{'Ratio':<{ratio_w}} | "
            f"{'Status':<{status_w}}"
        )

        print("\nProductivity Report")
        print(header)
        print("-" * len(header))

        for emp in employees_list:
            ratio_str = f"{emp.raw_productivity():.2f}"
            status_str = emp.clean_productivity()

            print(
                f"{emp.id:<{id_w}} | "
                f"{emp.name:<{name_w}} | "
                f"{ratio_str:<{ratio_w}} | "
                f"{status_str:<{status_w}}"
            )

    def calc_width(employees_list):
        if not employees_list:
            return 2, 4, 4, 5, 5, 5, 6  # Defaults for ID, Name, Role, Hours, Tasks, Ratio, Status

        id_w = max([len(str(emp.id)) for emp in employees_list] + [len("ID")])
        name_w = max([len(emp.name) for emp in employees_list] + [len("Name")])
        role_w = max([len(emp.role) for emp in employees_list] + [len("Role")])
        hours_w = max([len(f"{emp.hours_worked:.1f}") for emp in employees_list] + [len("Hours")])
        tasks_w = max([len(str(emp.tasks_completed)) for emp in employees_list] + [len("Tasks")])

        return id_w, name_w, role_w, hours_w, tasks_w

    def info(self, employees_list):
        id_w, name_w, role_w, hours_w, tasks_w = self.calc_width()

        print("\nID | Name | Role | Hours | Tasks")
        header = f"{'ID':<{id_w}} | {'Name':<{name_w}} | {'Role':<{role_w}} | {'Hours':<{hours_w}} | {'Tasks':<{tasks_w}}"

        print("\n" + header)
        print("-" * len(header))
        for emp in employees_list:
            hours_str = f"{emp.hours_worked:.1f}"
            print(
                f"{emp.id:<{id_w}} | "
                f"{emp.name:<{name_w}} | "
                f"{emp.role:<{role_w}} | "
                f"{hours_str:<{hours_w}} | "
                f"{emp.tasks_completed:<{tasks_w}}"
            )

    def update_info(self, employees_list):
        if not employees_list:
            print("\nNo employees to update info for.")
            return

        id = input("\nEmployee ID: ")

        target_emp = None
        for emp in employees_list:
            if str(emp.id) == id:
                target_emp = emp
                break
        if not target_emp:
            print(f"\nError: Employee with ID '{id}' not found.")
            return

        print(f"\nEditing data for: {target_emp.name} ({target_emp.id})"
              "\n1. Update Hours Worked"
              "\n2. Update Tasks Completed"
              "\n3. Update Role"
              "\n4. Remove employee"
              )

        choice = input("\nChoice: ")

        try:
            if choice == "1":
                print(f"\nEditing data for: {target_emp.name} ({target_emp.id})"
                     "\n1. Add amount of Hours"
                     "\n2. Remove amount of Hours"
                     "\n3. Set amount of Hours"
                      )

                hchoice = input("\nChoice: ")

                if hchoice == "1":
                    self.positive_float("Amount: ")
                    target_emp.hours_worked += val
                    print(f"\nSuccessfully Added {val} hours to worker {target_emp.id}")
                elif hchoice == "2":
                    self.positive_float("Amount: ")
                    target_emp.hours_worked -= val
                    print(f"\nSuccessfully removed {val} hours from worker {target_emp.id}")
                elif hchoice == "3":
                    self.positive_float("Amount: ")
                    target_emp.hours_worked = val
                    print(f"\nSuccessfully set {val} hours to worker {target_emp.id}")

            elif choice == "2":
                print(f"\nEditing data for: {target_emp.name} ({target_emp.id})"
                     "\n1. Add amount of Hours"
                     "\n2. Remove amount of Hours"
                     "\n3. Set amount of Hours"
                    )

                tchoice = input("\nChoice: ")

                if tchoice == "1":
                    added_hours = float(input("Amount: "))
                    if added_hours <= 0:
                        print("\nError: Amount cannot be negative.")
                    else:
                        target_emp.hours_worked += added_hours
                        print(f"\nSuccessfully Added {added_hours} hours to worker {target_emp.id}")
                elif tchoice == "2":
                    removed_hours = float(input("Amount: "))
                    if removed_hours <= 0:
                        print("\nError: Amount cannot be negative.")
                    else:
                        target_emp.hours_worked -= removed_hours
                        print(f"\nSuccessfully removed {removed_hours} hours from worker {target_emp.id}")
                elif tchoice == "3":
                    set_hours_worked = float(input("Amount: "))
                    if set_hours_worked <= 0:
                        print("\nError: Amount cannot be negative.")
                    else:
                        target_emp.hours_worked = set_hours_worked
                        print(f"\nSuccessfully set {set_hours_worked} hours to worker {target_emp.id}")
        except ValueError:
            print("\nError: Invalid input.")
"""

