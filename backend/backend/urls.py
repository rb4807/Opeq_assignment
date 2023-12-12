from django.contrib import admin
from django.urls import path
from .views import signup

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', signup, name='signup'),
]

