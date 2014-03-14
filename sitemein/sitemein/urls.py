from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'sitemein.views.home', name='home'),

    # user views
    url(r'^logout/$', 'sitemein.user_views.logout_view', name='logout'),
    url(r'^login/$', 'sitemein.user_views.login_view', name='login'),
    url(r'^register/$', 'sitemein.user_views.register_view', name='register'),
    url(r'^get_login_buttons/$', 'sitemein.user_views.get_login_buttons', name='get_login_buttons'),

    # url(r'^sitemein/', include('sitemein.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
