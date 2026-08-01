class Employee:
    def __init__(self, id, name, role, hours_worked, tasks_completed):
        self.id = id
        self.name = name
        self.role = role
        self.hours_worked = hours_worked
        self.tasks_completed = tasks_completed

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