from django.contrib import admin
from django.urls import include, path

from django.conf import settings
from django.conf.urls.static import static

from uploader.router import router as uploader_router

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
    path('api/', include(usuario_router.urls)),
    path("api/media/", include(uploader_router.urls)),
    ]

urlpatterns += static(settings.MEDIA_ENDPOINT, document_root=settings.MEDIA_ROOT)
