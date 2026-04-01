from django.urls import path
from .views import StudentIntegrationSummary

urlpatterns = [
    path('student-summary/<str:student_id>/', StudentIntegrationSummary.as_view(), name='student-summary'),
]
