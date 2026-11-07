from django.contrib import admin
from django.urls import path
from rest_framework.routers import SimpleRouter
from rest_framework.authtoken import views
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

from users.api.views import UserProfileExampleViewSet
from biblioteca.api.views import AutorViewSet, LivroViewSet


router = SimpleRouter()

router.register("users", UserProfileExampleViewSet, basename="users")
router.register("api/autores", AutorViewSet, basename="autores")
router.register("api/livros", LivroViewSet, basename="livros")


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/token-auth/", views.obtain_auth_token),
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "swagger/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui"
    ),
] + router.urls