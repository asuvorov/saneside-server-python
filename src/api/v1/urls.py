from django.conf.urls import include, url

from api.v1.views import *


urlpatterns = [
    url(r"^accounts/", include("api.v1.accounts.urls")),
    url(r"^blog/", include("api.v1.blog.urls")),
    url(r"^events/", include("api.v1.events.urls")),
    url(r"^forum/", include("api.v1.forum.urls")),
    url(r"^organizations/", include("api.v1.organizations.urls")),
]
