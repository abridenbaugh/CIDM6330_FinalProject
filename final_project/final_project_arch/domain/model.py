from datetime import date


class DomainSuccessionPlan:
    def __init__(self, employee):
        self.employee = DomainEmployee
        


class DomainEmployee:
    def __init__(self, id, name, level, succession_plan_needed, date_added):
        self.id = id
        self.name = name
        self.level = level
        self.succession_plan_needed = succession_plan_needed
        self.date_added = date_added

    def __str__(self):
        return f"{self.name}"



class DomainWorkOrder:
    def __init__(self, id, succession_plan_needed, date_added):
        self.id = id
        self.succession_plan_needed = succession_plan_needed
        self.date_added = date_added

    def __str__(self):
        return f"{self.id}"
