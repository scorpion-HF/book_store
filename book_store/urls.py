from django.contrib import admin
from django.urls import path, include, re_path, reverse
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from django.contrib.sitemaps import GenericSitemap
from django.contrib.sitemaps.views import sitemap
from django.contrib.sitemaps import Sitemap
from catalog.models import Book


class StaticViewSitemap(Sitemap):

    def items(self):
        return ['landing', 'about', 'contact', 'account_login', 'account_signup']

    def location(self, item):
        return reverse(item)


books_sitemap = {
    'queryset': Book.objects.all(),
    'date_field': 'date_of_publish',
}

sitemap_dict = {
    'books': GenericSitemap(books_sitemap),
    'static': StaticViewSitemap,
}

urlpatterns = [
                  path('', TemplateView.as_view(template_name='first_page.html'), name='landing'),
                  path('about/', TemplateView.as_view(template_name='about.html'), name='about'),
                  path('contact/', TemplateView.as_view(template_name='contact.html'), name='contact'),
                  re_path(r'^admin/login/?$', RedirectView.as_view(pattern_name='account_login')),
                  path('admin/', admin.site.urls),
                  path('accounts/', include('allauth.urls')),
                  path('captcha/', include('captcha.urls')),
                  path('user/', include('users.urls')),
                  path('catalog/', include('catalog.urls')),
                  path('comments_list/', include('commenting.urls')),
                  path('comments/', include('django_comments_xtd.urls')),
                  path('orders/', include('orders.urls')),
                  path('sitemap.xml', sitemap,
                       {'sitemaps': sitemap_dict},
                       name='django.contrib.sitemaps.views.sitemap'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
