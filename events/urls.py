from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add_event, name='add_event'),
    path('my-events/', views.my_events, name='my_events'),
    path('event/<int:pk>/', views.event_detail, name='event_detail'),

    # Admin Dashboard & Actions
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('approve/<int:event_id>/', views.approve_event, name='approve_event'),
    path('reject/<int:event_id>/', views.reject_event, name='reject_event'),
    path('featured/<int:event_id>/', views.toggle_featured, name='toggle_featured'),
    path('edit-admin/<int:event_id>/', views.edit_event_admin, name='edit_event_admin'),
    path('delete-admin/<int:event_id>/', views.delete_event_admin, name='delete_event_admin'),
]