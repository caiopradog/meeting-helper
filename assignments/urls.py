from django.urls import path

from . import views
from .views import LoginView

urlpatterns = [
    path("", views.index, name="assignments"),
    path("login", LoginView.as_view(), name="assignments.login"),
    path("logout", views.logout_view, name="assignments.logout"),
]
