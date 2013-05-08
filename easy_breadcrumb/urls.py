from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
     url(r'^$', 'easy_breadcrumb.views.home', name='home'),
     url(r'^section/$', 'easy_breadcrumb.views.section', name='section'),
     url(r'^section/subsection/$', 'easy_breadcrumb.views.sub_section',
         name='sub-section'),

    # url(r'^easy_breadcrumb/', include('easy_breadcrumb.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
