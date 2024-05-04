
from rest_framework import viewsets

from .models import Employee, SuccessionPlan
from .serializers import EmployeeSerializer, SuccessionPlanSerializer

# Create your views here.


class EmployeeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Employees to be viewed or edited
    """

    queryset = Employee.objects.all().order_by("-date_audited")
    serializer_class = EmployeeSerializer


class SuccessionPlanViewSet(viewsets.ModelViewSet):
    queryset = SuccessionPlan.objects.all()
    serializer_class = SuccessionPlanSerializer
