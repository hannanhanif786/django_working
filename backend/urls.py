
from django.contrib import admin
from django.urls import path, include
from user.views import TestingView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TestingView.as_view())
]
