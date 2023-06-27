# from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve

from first_django import settings
from first_django.views import page_500, page_404

urlpatterns = [
    #    path('admin/', admin.site.urls),
    path("hello/", include('helloworld.urls')),
    path('tmp/', include('tem_handler.urls')),
    path('account/', include('account.urls')),
    path('accounts/', include('accounts.urls')),
    path('grade/', include('grade.urls')),
]

handler500 = page_500
handler404 = page_404

if settings.DEBUG:
    urlpatterns += [
        re_path(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT
        }),
        path('__debug__/', include('debug_toolbar.urls'))
    ]
