from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
    path('fir/', include('fir.urls')),
    path('criminal/', include('criminal.urls')),
    path('cases/', include('casefiles.urls')),
    path('evidence/', include('evidence.urls')),
    path('court/', include('court.urls')),
    path('reports/', include('reports.urls')),
    path('stations/', include('stations.urls')),
    path('officers/', include('officers.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)