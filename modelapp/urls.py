from django.urls import path, include


from .views import *


urlpatterns = [
    
    path("register/", UserRegisteration.as_view()),
    path("login/", LoginView.as_view()),
    path("users/", UserListView.as_view()),
    path("users/<int:pk>/", UserDetailView.as_view()),
    path("verify/", VerifyView.as_view()),
]
