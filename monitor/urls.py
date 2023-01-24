from django.urls import path, include
from .views import CreateUrlAPIView, ListUrlAPIView


urlpatterns = [
    path('url/create/', CreateUrlAPIView.as_view()),
    path('url/get/', ListUrlAPIView.as_view()),

]