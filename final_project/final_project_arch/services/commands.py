import sys
from abc import ABC, abstractmethod
from datetime import datetime
from injector import Injector, inject
import pytz

import requests
from django.db import transaction

from succession_plans.models import SuccessionPlan, Employee, WorkOrder
from final_project_arch.domain.model import DomainSuccessionPlan, DomainEmployee, DomainWorkOrder

class Command(ABC):
    @abstractmethod
    def execute(self, data):
        raise NotImplementedError("A command must implement the execute method")

class PythonTimeStampProvider:
    def __init__(self):
        self.now = datetime.now(pytz.UTC).isoformat()

class 