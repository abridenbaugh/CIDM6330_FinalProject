from django.urls import include, path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r"employee", views.EmployeeViewSet)
router.register(r"successionplan", views.SuccessionPlanViewSet)

app_name = "succession_plans"

urlpatterns = [
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path("", include(router.urls)),
]

# add the router's URLs to the urlpatterns
urlpatterns += router.urls