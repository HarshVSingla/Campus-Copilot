from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from home import views as home_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('exam-calendar/', include('exam_calender.urls')),
    path('', include('announcement.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='announcements/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
