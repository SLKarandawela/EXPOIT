from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # exhibition urls
    path('exhibition/', include('Exhibition.urls')),
    # exhibition auth url
    path('', include('ExhibitionAuth.urls')),

]

urlpatterns += static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
)
