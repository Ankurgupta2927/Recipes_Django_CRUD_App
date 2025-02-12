from django.contrib import admin
from django.urls import path , include
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path("Add/",views.index,name="index"),
    path("delete_receipe/<id>/",views.delete_receipe,name="delete_receipe"),
    path("update_receipe/<id>/",views.update_receipe,name="update_receipe"),
    path("",views.serach,name="search"),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)


urlpatterns += staticfiles_urlpatterns()