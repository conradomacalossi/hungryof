from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

import core.views
import catalog.views


urlpatterns = [
    url(r'^$', core.views.index, name='index'),
    url(r'^menu/', catalog.views.menu, name='menu'),
    url(r'^admin/', include(admin.site.urls)),
]
