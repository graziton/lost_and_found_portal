from django.urls import path
from .views import (
    home, report_lost, report_found, items_list, lost_item_detail, found_item_detail, register, profile,
    LostItemUpdateView, LostItemDeleteView, FoundItemUpdateView, FoundItemDeleteView
)

urlpatterns = [
    path('', home, name='home'),
    path('report-lost/', report_lost, name='report_lost'),
    path('report-found/', report_found, name='report_found'),
    path('items/', items_list, name='items_list'),
    path('lost-item/<int:pk>/', lost_item_detail, name='lost_item_detail'),
    path('found-item/<int:pk>/', found_item_detail, name='found_item_detail'),
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
    path('lost-item/<int:pk>/edit/', LostItemUpdateView.as_view(), name='lost_item_update'),
    path('lost-item/<int:pk>/delete/', LostItemDeleteView.as_view(), name='lost_item_delete'),
    path('found-item/<int:pk>/edit/', FoundItemUpdateView.as_view(), name='found_item_update'),
    path('found-item/<int:pk>/delete/', FoundItemDeleteView.as_view(), name='found_item_delete'),
]
