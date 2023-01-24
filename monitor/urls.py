from django.urls import path, include
from .views import CreateUrlAPIView


urlpatterns = [
    path('url/create/', CreateUrlAPIView.as_view()),
]