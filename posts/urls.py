from django.urls import path, include
from .views import PostList, PostDetaiil

urlpatterns = [
    path('<int:pk>', PostDetaiil.as_view()),
    path('', PostList.as_view()),
]