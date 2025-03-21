from django.contrib import admin
from django.urls import path, include
from users.views import home  # Import the home view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('persons/', include('persons.urls')),
    path('medications/', include('medications.urls')),
    path('prescriptions/', include('prescriptions.urls')),
    path('', home, name='home'),
]