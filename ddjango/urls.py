from django.contrib import admin
from django.urls import path
from ddjango.views import home2
from ddjango.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('produtos2/', home2),
    path('produtos/', home),
]
