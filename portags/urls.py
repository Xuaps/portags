from django.conf.urls.defaults import *
from portags.models import Tag
import settings

info_dict = {
    'queryset': Tag.objects.all(),
}

urlpatterns = patterns('',
    (r'^$', 'django.views.generic.list_detail.object_list', info_dict),
    (r'^search/$', 'portags.views.search'),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^site_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': 'portags/static/'})
    )