from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import CommentViewSet, PostViewSet, GroupViewSet, FollowViewSet

router = DefaultRouter()
router.register('posts', PostViewSet, basename='posts')
router.register('group', GroupViewSet, basename='groups')
router.register('follow', FollowViewSet, basename='follows')
router.register(
    r'posts/(?P<post_id>\d+)/comments', CommentViewSet, basename='comments'
)

urlpatterns = [
    path('api/v1/token/', TokenObtainPairView.as_view(),
            name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(),
            name='token_refresh'),
    path('', include(router.urls))
]
