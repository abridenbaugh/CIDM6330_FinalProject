from django.db import transaction
from django.test import TestCase
from django.urls import reverse
from django.utils.timezone import localtime

from succession_plans.models import Employee, SuccessionPlan
from final_project_arch.domain.model import DomainEmployee, DomainSuccessionPlan
from final_project_arch.services.commands import (
    AddEmployeeCommand,
    EmployeeNeedsSuccessionPlanCommand,
    AddSuccessionPlanCommand,
    EditSuccessionPlanCommand,
)


class TestEmployeeCommands(TestCase):
    def setUp(self):
        right_now = localtime().date()

        self.domain_employee_1 = DomainEmployee(
            id=1,
            name="Allie Walker",
            level=7,
            succession_plan_needed=True,
            date_audited=right_now,
        )

        self.domain_employee_2 = DomainEmployee(
            id=2,
            name="Bill Bridenbaugh",
            level=3,
            succession_plan_needed=True,
            date_audited=right_now,
        )

    def test_command_add_employee(self):
        add_command = AddEmployeeCommand()
        add_command.execute(self.domain_employee_1)

        self.assertEqual(Employee.objects.count(), 1)

        self.assertEqual(Employee.objects.get(id=1).name,
                         self.domain_employee_1.name)

    def test_command_employee_needs_succession_plan(self):
        add_command = AddEmployeeCommand()
        add_command.execute(self.domain_employee_1)
        add_command.execute(self.domain_employee_2)

        def test_needs_succession_plan(self):
            needs_succession_plan_command = EmployeeNeedsSuccessionPlanCommand()
            needs_succession_plan_command.execute(self.domain_employee_1)
            needs_succession_plan_command.execute(self.domain_employee_2)

            self.assertEqual(Employee.objects.get(
                id=1).succession_plan_needed, False)
            self.assertEqual(Employee.objects.get(
                id=2).succession_plan_needed, True)


class TestSuccessionPlanCommands(TestCase):
    def setUp(self):
        right_now = localtime().date()

        self.domain_employee_1 = DomainEmployee(
            id=1,
            name="Allie Walker",
            level=7,
            succession_plan_needed=True,
            date_audited=right_now,
        )

        self.domain_employee_2 = DomainEmployee(
            id=2,
            name="Bill Bridenbaugh",
            level=3,
            succession_plan_needed=True,
            date_audited=right_now,
        )

        self.domain_succession_plan = DomainSuccessionPlan(
            id=1,
            notes="Just promoted",
            employee=Employee(),
            date_added = right_now,
        )

    def test_succession_plan_add_command(self):
        add_command= AddEmployeeCommand()
        add_command.execute(self.domain_employee_2)

        def test_add_succession_plan(self):
            add_succession_plan_command= AddSuccessionPlanCommand()
            add_succession_plan_command.execute(self.domain_succession_plan)

            self.assertEqual(SuccessionPlan.objects.count(), 1)

    def test_succession_plan_edit_command(self):
        add_command = AddEmployeeCommand()
        add_command.execute(self.domain_employee_2)

        def test_add_and_edit_succession_plan(self):
            add_succession_plan_command = AddSuccessionPlanCommand()
            add_succession_plan_command.execute(self.domain_succession_plan_1)

            self.domain_succession_plan_1.notes = "Update succession plan"

            edit_succession_plan_command = EditSuccessionPlanCommand()
            edit_succession_plan_command.execute(self.domain_succession_plan_1)

            self.assertEqual(SuccessionPlan.objects.get(
                id=1).notes, "Update succession plan")
