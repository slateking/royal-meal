from django.urls import path, include
from authentication.views import UserCreateView, UserDetailView

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),  # Enable login/logout views
    path('api/users/', UserCreateView.as_view()),       # Register new user
    path('api/users/<int:pk>/', UserDetailView.as_view()),  # Retrieve/update user
]
