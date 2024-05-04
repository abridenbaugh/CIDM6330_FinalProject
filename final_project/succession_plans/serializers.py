from .models import Employee, SuccessionPlan
from django.contrib.auth.models import User
from rest_framework import serializers

class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta: 
        model = Employee
        fields = ("id", "name", "level", "succession_plan_needed", "date_audited")
    
    # employees = serializers.PrimaryKeyRelatedField(many=True, queryset=Employee.objects.all())


class SuccessionPlanSerializer(serializers.ModelSerializer):
    succession_plan = serializers.PrimaryKeyRelatedField(many=True, queryset=SuccessionPlan.objects.all())