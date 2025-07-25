from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('services/<str:pk>/', views.service_detail, name='service-detail'),
    path('facilities/', views.facilities, name='facilities'),
    path('certificates/', views.certificates, name='certificates'),
    path('blogs/', views.blog, name='blog'),
    path('blogs/<str:pk>/', views.blog_detail, name='blog-detail'),
    path('contact/', views.contact, name='contact'),
    path('test-newsletter/', views.test_newsletter, name='test_newsletter'), 
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
