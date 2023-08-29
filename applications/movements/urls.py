from django.urls import include, path
from .routers import router

app_name = "movements_app"

urlpatterns = [
    path("", include(router.urls)),
]
