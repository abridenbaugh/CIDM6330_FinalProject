from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight

from final_project_arch.domain.model import DomainEmployee, DomainSuccessionPlan, DomainWorkOrder

# pygments stuff
LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])

# Create your models here.
class SuccessionPlan:
    pass


class Employee(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    level = models.IntegerField()
    succession_plan_needed = models.BooleanField(SuccessionPlan)
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"


class WorkOrder(models.Model):
    id = models.IntegerField(primary_key=True)
    succession_plan_needed = models.BooleanField(SuccessionPlan)
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.id}"

    class Meta:
        app_label = "succession_plans"
