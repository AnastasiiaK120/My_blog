# from django.urls import path, include
# from .views import (PostList, PostDetaiil, UserDetail, UserList,)
#


# urlpatterns = [
#     path('users/', UserList.as_view()),
#     path('users/<int:pk>/', UserDetail.as_view()),
#
#     path('<int:pk>', PostDetaiil.as_view()),
#     path('', PostList.as_view()),
# ]

from rest_framework.routers import SimpleRouter
from .views import PostViewSet, UserViewSet

router = SimpleRouter()

router.register('users', UserViewSet, basename='users')
router.register('', PostViewSet, basename='posts')

urlpatterns = router.urls