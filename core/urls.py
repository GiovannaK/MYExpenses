
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = 'MYExpenses Adminstração'
admin.site.site_title = 'MYExpenses'
admin.site.index_title = 'Bem-Vindo(a)'

urlpatterns = [
    path('', include('expenses.urls')),
    path('profile/', include('profiles.urls')),
    path('accounts/', include('accounts.urls')),
    path('earns/', include('earns.urls')),
    path('expenses_dashboard/', include('expenses_dashboard.urls')),
    path('earnings_dashboard/', include('earnings_dashboard.urls')),
    path('admin/', admin.site.urls),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
