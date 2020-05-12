from . import views

from django.contrib import admin
from django.urls import path
from products.views import ProductListView
from django.urls import include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    # path ('', views.index, name="index"),
    path('', ProductListView.as_view(), name="index"),
    path('users/login', views.login_view, name="login"),
    path('users/logout', views.logout_view, name="logout"),
    path('users/registro', views.registro, name="registro"),
    path('admin/', admin.site.urls),
    path('productos/', include('products.urls')),
    path('carrito/', include('carts.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
