from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>/', views.prescription_detail, name='prescription_detail'),
]