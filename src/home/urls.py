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

    # -------------------------------------------------------------------------
    # --- Terms & Conditions
    url(r"^privacy-policy/$",
        privacy_policy,
        name="privacy-policy"),
    url(r"^user-agreement/$",
        user_agreement,
        name="user-agreement"),
]
