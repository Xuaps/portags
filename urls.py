from django.conf.urls.defaults import *
from django.contrib import admin
from portags.models import Tag
import settings

admin.autodiscover()

info_dict = {
    'queryset': Tag.objects.all(),
}

urlpatterns = patterns('',
    (r'^$', 'django.views.generic.list_detail.object_list', info_dict),
    (r'^search/$', 'portags.views.search'),
    (r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': 'portags/static/'})
    )