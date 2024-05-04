# import pytz
# from datetime import datetime

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIRequestFactory, APITestCase

from . import utils
from .models import Employee, SuccessionPlan


class EmployeeTests(APITestCase):
    # date = datetime.now(pytz.UTC).isoformat()

    def setUp(self):
        self.factor = APIRequestFactory
        self.employee = Employee.objects.create(
            id=1,
            name="Allie Walker",
            level=7,
            succession_plan_needed=False,
            date_audited="2024-5-1",
        )

        self.list_url = reverse("succession_plans:employee-list")
        self.detail_url = reverse(
            "succession_plans:employee-detail", kwargs={"pk": self.employee.id}
        )

    def test_create_employee(self):
        data = {
            "id": 10,
            "name": "Eric Walker",
            "level": 7,
            "succession_plan_needed": False,
            "date_audited": "2024-5-2",
        }
        response = self.client.post(self.list_url, data, format="json")
        self.assertTrue(status.is_success(response.status_code))
        self.assertEqual(Employee.objects.count(), 2)
        self.assertEqual(Employee.objects.get(id=10).name, "Eric Walker")

    def test_audit_employees(self):
        data = {
            "id": 5,
            "name": "Bill Bridenbaugh",
            "level": 3,
            "succession_plan_needed": True,
            "date_audited": "2024-5-2"
        }

        response = self.client.post(self.list_url, data, format="json")
        self.assertTrue(status.is_success(response.status_code))

        utils.audit()

        self.assertTrue(Employee.objects.get(id=1).date_audited,
                        Employee.objects.get(id=5).date_audited)


class SuccessionPlanTests(APITestCase):
    # date = datetime.now(pytz.UTC).isoformat()
    def setUp(self):
        self.factor = APIRequestFactory
        self.employee = Employee.objects.create(
            id=5,
            name="Bill Bridenbaugh",
            level=3,
            succession_plan_needed=True,
            date_audited="2024-5-1",
        )

        def setUp(self):
            self.factor = APIRequestFactory
            self.succession_plan = SuccessionPlan.objects.create(
                id=5,
                employee=Employee(),
                notes="recently promoted",
                date_added="2024-5-2",
            )

            self.list_url = reverse("succession_plans:succession_plan-list")
            self.detail_url = reverse(
                "succession_plans:succession_plan-detail", kwargs={"pk": self.succession_plan.id}
            )

        def test_add_succession_plan(self):
            data = {
                "id": 2,
                "employee": Employee(),
                "notes": "Recent promotion",
                "date_added": "2024-5-2",
            }

            response = self.client.post(self.list_url, data, format="json")
            self.assertTrue(status.is_success(response.status_code))
            self.assertEqual(self.SuccessionPlan.objects.count(), 2)
