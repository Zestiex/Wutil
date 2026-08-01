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

    def info(self):
        pass