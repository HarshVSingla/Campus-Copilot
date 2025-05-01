from django.urls import path
from django.views.static import serve
from django.conf import settings
from . import views

app_name = 'exam_calender'

urlpatterns = [
    path('/exam_calender', views.exam_calendar, name='exam_calendar'),
    path('send-email-notification/', views.send_email_notification, name='send_email_notification'),
]