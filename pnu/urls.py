from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

# FIXME: 이 코드는 RedirectView에 의해서 제거될 것입니다.
from django.shortcuts import render, resolve_url
def root(request):
    앱_소개 = [
        {"주소": resolve_url("blog:post_list"), "설명": "블로그 서비스입니다"},
        {"주소": resolve_url("shop:shop_list"), "설명": "가게 소개 서비스입니다"},
        {"주소": resolve_url("travel:post_list"), "설명": "여행 서비스입니다"},
    ]
    return render(request, 'root.html', {'앱_소개': 앱_소개})

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
