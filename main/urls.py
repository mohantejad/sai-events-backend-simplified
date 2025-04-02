from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .auth_views import signup_view, UserRetrieveView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenBlacklistView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/tokens/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/jwt/blacklist/', TokenBlacklistView.as_view(), name='token_blacklist'),
    path('auth/signup/', signup_view, name='signup'),
    path('auth/user/', UserRetrieveView.as_view(), name='user-retrieve'),
    path('', include('events.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
