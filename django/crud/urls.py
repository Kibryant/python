from django.urls import path
from app_crud import views

urlpatterns = [
    # routes, views, reference
    path("", views.home, name="home"),
    path("create_user", views.create_user, name="create_user"),
    # path("users", views.users, name="users"),
]
