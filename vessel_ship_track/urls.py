from django.contrib import admin
from django.urls import include, path
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('tracking.urls')),
]

urlpatterns = format_suffix_patterns(urlpatterns)

