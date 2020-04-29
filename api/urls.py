from django.urls import path, include
from .views import PostViewSet, CommentViewSet, FollowViewSet, GroupViewSet
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
        TokenObtainPairView,
        TokenRefreshView,
    )

router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'posts/(?P<post_id>\d+)/comments', CommentViewSet)
router.register(r'follow', FollowViewSet, basename="Follow")
router.register(r'group', GroupViewSet, basename="Group")

urlpatterns = [
    path('', include(router.urls)),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
