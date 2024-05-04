import sys
from abc import ABC, abstractmethod
from datetime import datetime
import pytz

import requests
from django.db import transaction

from succession_plans.models import SuccessionPlan, Employee
from final_project_arch.domain.model import DomainSuccessionPlan, DomainEmployee


class Command(ABC):
    @abstractmethod
    def execute(self, data):
        raise NotImplementedError(
            "A command must implement the execute method")


class AddEmployeeCommand(Command):
    def execute(self, data: DomainEmployee):
        employee = Employee(data.id, data.name, data.level,
                            data.succession_plan_needed, data.date_audited)
        with transaction.atomic():
            employee.save()


# class DeleteEmployeeCommand(Command):
#     def execute(self, data: DomainEmployee):
#         employee = Employee.objects.get(id=data.id)
#         with transaction.atomic():
#             employee.delete()

# class RunAuditCommand(Command):
#     def execute(self, data):
#         return super().execute(data)


class EmployeeNeedsSuccessionPlanCommand(Command):
    def execute(self, data: DomainEmployee):
        level = Employee.level
        if level != 1 and level != 2 and level != 3:
            pass
        else:
            Employee.succession_plan_needed = True
            employee = Employee.update_from_domain(data)
            with transaction.atomic():
                employee.save()


class AddSuccessionPlanCommand(Command):
    def execute(self, data: DomainSuccessionPlan):
        succession_plan_needed = Employee.succession_plan_needed
        if succession_plan_needed is False:
            pass
        else:
            succession_plan = SuccessionPlan(
            id=data.id, employee=data.employee, notes=data.notes, date_added=data.date_added)
            with transaction.atomic():
                succession_plan.save()


class EditSuccessionPlanCommand(Command):
    def execute(self, data: DomainSuccessionPlan):
        succession_plan = SuccessionPlan.update_from_domain(data)
        with transaction.atomic():
            succession_plan.save()
