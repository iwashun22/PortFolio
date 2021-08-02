from django.contrib import admin
from django.urls import path, include
from django.conf import settings             # add this
from django.conf.urls.static import static   # add this

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", include('core.urls'))
]