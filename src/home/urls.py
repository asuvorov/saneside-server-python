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

    # -------------------------------------------------------------------------
    # --- Terms & Conditions
    url(r"^privacy-policy/$",
        PrivacyPolicyViewSet.as_view(),
        name="privacy-policy"),
    # url(r"^user-agreement/$",
    #     user_agreement,
    #     name="user-agreement"),
]
