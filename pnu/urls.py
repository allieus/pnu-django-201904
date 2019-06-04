from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

# FIXME: 이 코드는 RedirectView에 의해서 제거될 것입니다.
from django.shortcuts import redirect
def root(request):
    return redirect("shop:shop_list")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('weblog/', include('blog.urls')),
    path('shop/', include('shop.urls')),
    path('travel/', include('travel.urls')),
    path('', root, name='root'),
]

urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
