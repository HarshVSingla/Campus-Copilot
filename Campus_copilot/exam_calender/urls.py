from django.urls import path
from . import views

app_name = 'exam_calender'

urlpatterns = [
    path('/exam_calender', views.exam_calendar, name='exam_calendar'),
]