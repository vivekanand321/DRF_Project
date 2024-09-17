

from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from django.conf import settings
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', include('app.urls')),
    path('api/courses/', include('courses.urls',namespace="courses")),

]
if settings.DEBUG:
    import debug_toolbar
    urlpatterns+=[
        path('__debug__/',include(debug_toolbar.urls))
    ]