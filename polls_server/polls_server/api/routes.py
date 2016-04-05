from django.conf.urls import url, include
from views import HelloAPI

routes = [
    url(r'^api/hello/$', HelloAPI.as_view()),
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework'))
]
