from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='flatpages/default.html'), name='default'),
    path('admin/', admin.site.urls),
    path('about/', TemplateView.as_view(template_name='about.html'), name='about'),
    path('contact_page/', TemplateView.as_view(template_name='contact_page.html'), name='contact'),
]