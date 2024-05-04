from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight

from final_project_arch.domain.model import DomainEmployee, DomainSuccessionPlan

# pygments stuff
LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])

# Create your models here.


class Employee(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    level = models.IntegerField()
    succession_plan_needed = models.BooleanField()
    date_audited = models.DateField()

    def __str__(self):
        return f"{self.name}"

    class Meta:
        app_label = "succession_plans"

    @staticmethod
    def update_from_domain(domain_employee: DomainEmployee):
        try:
            employee = Employee.objects.get(id=domain_employee.id)
        except Employee.DoesNotExist:
            employee = Employee(id=domain_employee.id)

        employee.id = domain_employee.id
        employee.name = domain_employee.name
        employee.level = domain_employee.level
        employee.succession_plan_needed = domain_employee.succession_plan_needed
        employee.date_audited = domain_employee.date_audited
        employee.save()

    def to_domain(self) -> DomainEmployee:
        b = DomainEmployee(
            id=self.id,
            name=self.name,
            level=self.level,
            succession_plan_needed=self.succession_plan_needed,
            date_audited=self.date_audited,
        )
        return b


class SuccessionPlan(models.Model):
    id = models.IntegerField(primary_key=True)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    notes = models.CharField(max_length=255)
    date_added = models.DateField()

    class Meta:
        app_label = "succession_plans"

    @staticmethod
    def update_from_domain(domain_succession_plan: DomainSuccessionPlan):
        try:
            succession_plan = SuccessionPlan.objects.get(
                id=domain_succession_plan.id)
        except SuccessionPlan.DoesNotExist:
            succession_plan = SuccessionPlan(
                id=domain_succession_plan.id)

        succession_plan.id = domain_succession_plan.id
        succession_plan.employee = domain_succession_plan.employee
        succession_plan.notes = domain_succession_plan.notes
        succession_plan.date_added = domain_succession_plan.date_added
        succession_plan.save()

    def to_domain(self) -> DomainSuccessionPlan:
        b = DomainSuccessionPlan(
            id=self.id,
            employee=self.employee,
            notes=self.notes,
            date_added=self.date_added,
        )
        return b


# class WorkOrder(models.Model):
#     id = models.IntegerField(primary_key=True)
#     succession_plan_needed = models.BooleanField(SuccessionPlan)
#     date_added = models.DateField(auto_now_add=True)

#     def __str__(self):
#         return f"{self.id}"

#     class Meta:
#         app_label = "succession_plans"
