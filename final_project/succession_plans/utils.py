import pytz
from datetime import datetime

from .models import Employee, SuccessionPlan


def audit():
    employee = Employee.objects.all()
    date = datetime.now(pytz.UTC)
    for i in employee:
        i.date_audited = date
        i.save()
