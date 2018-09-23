from django.conf.urls import url

from home.views import *


urlpatterns = [
    # -------------------------------------------------------------------------
    # --- DESKTOP
    # -------------------------------------------------------------------------
    # --- Index
    url(r"^$",
        index,
        name="index"),
]
