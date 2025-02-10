from django.urls import path
from .views import home, report_lost, report_found, items_list

urlpatterns = [
    path('', home, name='home'),
    path('report-lost/', report_lost, name='report_lost'),
    path('report-found/', report_found, name='report_found'),
    path('items/', items_list, name='items_list'),
]
