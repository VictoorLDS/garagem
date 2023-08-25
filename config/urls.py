from django.contrib import admin
from django.urls import include, path

from usuario.router import router as usuario_router

from rest_framework.routers import DefaultRouter

from garagem.views import AcessorioViewSet, CategoriaViewSet, CorViewSet, MarcaViewSet, ModeloViewSet, VeiculoViewSet

router = DefaultRouter()
router.register(r"acessorio", AcessorioViewSet)
router.register(r"categoria", CategoriaViewSet)
router.register(r"cor", CorViewSet)
router.register(r"marca", MarcaViewSet)
router.register(r"modelo", ModeloViewSet)
router.register(r"veiculo", VeiculoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", include(usuario_router.urls)),
]
