from django.urls import path
from .views import home, report_lost, report_found

urlpatterns = [
    path('', home, name='home'),
    path('report-lost/', report_lost, name='report_lost'),
    path('report-found/', report_found, name='report_found'),
]
