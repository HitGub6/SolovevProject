from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from AnalyticApp import views

urlpatterns = [
    path("", views.index),
    path("demand/", views.demand),
    path("geography/", views.geography),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
