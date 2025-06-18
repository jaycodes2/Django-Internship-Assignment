from django.urls import path
from .views import public_view, protected_view
from .views import public_view, register_user
urlpatterns = [
    path('public/', public_view, name='public'),
    path('register/', register_user, name='register'),
]
