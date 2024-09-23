from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import main, verifica_email

urlpatterns = [
    path('', main, name='Porfolio'),
    path('success/', main, name='success'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
