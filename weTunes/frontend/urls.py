from django.conf.urls.defaults import *


urlpatterns = patterns('',
    # actual frontend stuff
    (r'^vote/(?P<filename>.*)$', 'frontend.views.vote'),
    (r'^unvote/(?P<filename>.*)$', 'frontend.views.unvote'),
    # important to preserve the garunteed field because it is not checked again
    (r'^search/(?P<field>(artist|title|album|any))/(?P<value>.*)$', 'frontend.views.search'),
    (r'^setvolume/(?P<level>\d{1,3})$', 'frontend.views.setvolume'),
    (r'^playpause$', 'frontend.views.playpause'),
    (r'^updatedb$', 'frontend.views.updatedb'),

    # login stuff
    (r'^accounts/login$', 'django.contrib.auth.views.login', {'template_name': 'account/login.html'}),
    (r'^accounts/logout$', 'django.contrib.auth.views.logout', {'template_name': 'account/logout.html'}),

    # default
    (r'^$', 'frontend.views.index'),

    # Example:
    # (r'^weTunes/', include('weTunes.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
)
