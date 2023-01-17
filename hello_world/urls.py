
from django.contrib import admin
from django.urls import path
from app.simple_app import views
urlpatterns = [
    path('',views.index ,name='index'),
    path('bmi/',views.bmi, name='bmi'),
    path('admin/', admin.site.urls),
]
