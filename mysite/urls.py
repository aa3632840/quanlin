from django.conf.urls import patterns, include, url
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
import xadmin
admin.autodiscover()
xadmin.autodiscover()
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', '{{ project_name }}.views.home', name='home'),
    # url(r'^{{ project_name }}/', include('{{ project_name }}.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(xadmin.site.urls)),
    #url(r'^xadmin/', include(xadmin.site.urls)),
    #url(r'^polls/', include('polls.urls',namespace='polls')),
    url(r'^quanlinx/', include('quanlin.urls',namespace='quanlin')),
    

)