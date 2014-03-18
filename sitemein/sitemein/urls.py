from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'sitemein.views.home', name='home'),
    url(r'^create-site/$', 'sitemein.views.create_site', name='create_site'),
    url(r'^create-site/success/$', 'sitemein.views.create_site_success', name='create_site_success'),
    url(r'^about/$', 'sitemein.views.about', name='about'),
    url(r'^features/$', 'sitemein.views.features', name='features'),
    url(r'^price-list/$', 'sitemein.views.price_list', name='price_list'),
    url(r'^work/$', 'sitemein.views.work', name='work'),

    # user views
    url(r'^logout/$', 'sitemein.user_views.logout_view', name='logout'),
    url(r'^login/$', 'sitemein.user_views.login_view', name='login'),
    url(r'^register/$', 'sitemein.user_views.register_view', name='register'),
    url(r'^get_login_buttons/$', 'sitemein.user_views.get_login_buttons', name='get_login_buttons'),

    # url(r'^sitemein/', include('sitemein.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('', (r'^static/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.STATIC_ROOT, 'show_indexes': True}))

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
