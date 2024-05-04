import csv
from pathlib import Path
from random import randint

from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

from django.core.files import File
from django.db.models.signals import post_save

from .consumers import SuccessionPlanConsumer
from .models import Employee, SuccessionPlan

channel_layer = get_channel_layer()


def log_employees_who_need_succession_plan_to_csv(sender, instance, **kwargs):
    print("Succession plan needed signal: CSV")

    if Employee.succession_plan_needed is False:
        pass
    else:
        file = Path(__file__).parent.parent / "final_project_arch" / \
            "domain" / "created_log.csv"
        print(f"Writing to {file}")

        with open(file, "a+", newline="") as csvfile:
            logfile = File(csvfile)
            logwriter = csv.writer(
                logfile,
                delimiter=",",
            )

            logwriter.writerow(
                [
                    instance.id,
                    instance.name,
                    instance.level,
                    instance.succession_plan_needed,
                    instance.date_audited,
                ]
            )


def send_employee_list_to_channel(sender, instance, **kwargs):
    print("Employee list signal: Channel")
    print(f"Sending employee list to channel: {instance}")
    if Employee.succession_plan_needed is True:
        async_to_sync(channel_layer.send)(
            "succession_plan_needed", {
                "type": "print.employee.list", "data": instance.name}
        )
    else:
        pass


# # connect the signal to this receiver
post_save.connect(
    log_employees_who_need_succession_plan_to_csv, sender=Employee)
post_save.connect(send_employee_list_to_channel, sender=Employee)
