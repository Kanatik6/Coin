from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,)
from accounts.views import UserViewSet
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('user',UserViewSet,basename='user')


urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
urlpatterns +=router.urls
