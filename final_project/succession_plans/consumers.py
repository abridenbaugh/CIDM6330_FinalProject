# Django
from channels.consumer import AsyncConsumer

# Local
from succession_plans.models import Employee


class SuccessionPlanConsumer(AsyncConsumer):
    async def print_employee_list(self, message):
        print(f"WORKER: Employee needs succession plan: {message['data']}")
