from django.conf.urls import include, url
from django.contrib import admin
from blog.models import *
from cms.sitemaps import CMSSitemap
from django.conf.urls import url
from django.contrib.sitemaps.views import sitemap
from sitemaps import BlogSitemap

sitemaps = {
    'static': sitemap,
    'blog':BlogSitemap,

}

urlpatterns =[
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('blog.urls')),
    url(r'^sitemap.xml', include('sitemaps.urls')),

]
