from django.contrib import admin
from django.urls import path, include
from home import views as home_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('exam-calendar/', include('exam_calender.urls')),
]
