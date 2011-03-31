from django.conf.urls.defaults import *
from portags.models import Tag
from portags.models import HtmlFontSizer


urlpatterns = patterns('',
    (r'^$', 'portags.views.list'),
    (r'^search/$', 'portags.views.search'),
)