# contact/urls.py
from django.urls import path
from .views import contact_view, success_view

urlpatterns = [
    path('', contact_view, name='contact'), # or "contact/"
    path('success/', success_view, name='success'), # The 'name' here must match your redirect
]