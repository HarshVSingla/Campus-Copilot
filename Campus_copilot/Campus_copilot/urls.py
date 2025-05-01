from django.contrib import admin
from django.urls import path, include
from home import views as home_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_views.home, name='home'),  # Default landing page
    path('exam-calendar/', include('exam_calender.urls')),  # Exam calendar URLs
]
