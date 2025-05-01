from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('announcement/<int:announcement_id>/', views.view_announcement, name='view_announcement'),
    path('admin/dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('admin/announcement/create/', views.create_announcement, name='create_announcement'),
    path('admin/announcement/<int:announcement_id>/edit/', views.edit_announcement, name='edit_announcement'),
    path('admin/announcement/<int:announcement_id>/delete/', views.delete_announcement, name='delete_announcement'),
]