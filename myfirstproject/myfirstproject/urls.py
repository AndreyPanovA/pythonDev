from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
import events.views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', views.about),
    # path('', views.about),
    path('posts/', include('blog.urls')),
    path('', events.views.home),
    path('reversed', views.reverse, name='reverse')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
