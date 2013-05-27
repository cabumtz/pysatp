from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pysatp.views.home', name='home'),
    # url(r'^pysatp/', include('pysatp.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    # url(r'^satp/choferes/', 'transpu.views'),

    url(r'^satp/$', 'transpu.views.index'),
    url(r'^satp/index\.html$', 'transpu.views.index'),

    url(r'^satp/entidades\.html$', 'transpu.views.entidades'),
    url(r'^satp/evaluacion\.html$', 'transpu.views.evaluacion'),
    url(r'^satp/reportes\.html$', 'transpu.views.reportes'),
    url(r'^satp/job1\.html$', 'transpu.views.job1Test'),
)
