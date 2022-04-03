
from django.urls import path
from .views import UserRegisterView

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    
  
]

# post/<int:pk> identifies each post with pk and gives each post uniqueness 