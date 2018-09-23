from django.conf.urls import (
    include,
    url,
    )

from .views import *


urlpatterns = [
    url(r"^status/",
        api_status,
        name="api-status"),
    url(r"^version/",
        api_version,
        name="api-version"),

    url(r"^v1/", include("api.v1.urls")),
]
