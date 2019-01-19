from django.conf.urls import url

from home.views import *


urlpatterns = [
    # -------------------------------------------------------------------------
    # --- DESKTOP
    # -------------------------------------------------------------------------
    # --- Index
    url(r"^$",
        IndexViewSet.as_view(),
        name="index"),
]
