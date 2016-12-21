from django.conf.urls import url, include
from django.conf import settings
from django.contrib import admin

# --------------------------------------
# Base URLS
# --------------------------------------
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

# --------------------------------------
# Misc API URLS
# --------------------------------------
urlpatterns += [
    url(r'^%s' % settings.API_PATH, include('misc_api.urls')),
]

# --------------------------------------
# Debug toolbar
# --------------------------------------
if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
