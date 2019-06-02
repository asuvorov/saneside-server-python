import inspect

from django.shortcuts import (
    get_object_or_404,
    redirect,
    render,
    )
from django.views.decorators.cache import cache_page
from django.views.generic import TemplateView

from termcolor import colored


# -----------------------------------------------------------------------------
# --- Index.
# -----------------------------------------------------------------------------
# @cache_page(60 * 60)
class IndexViewSet(TemplateView):
    """Index Page View Set."""

    template_name = "home/index.html"

    def get(self, request, *args, **kwrags):
        """GET."""
        print colored("***" * 27, "green")
        print colored("*** INSIDE `{}.{}`".format(
            self.__class__.__name__,
            inspect.stack()[0][3]
            ), "green")

        # g = GeoIP()
        # ip = get_client_ip(request)
        # # ip = "108.162.209.69"
        # country = g.country(ip)
        # city = g.city(ip)

        # print colored("[---  DUMP   ---] COUNTRY : %s" % country, "yellow")
        # print colored("[---  DUMP   ---] CITY    : %s" % city, "yellow")

        return self.render_to_response({})


# -----------------------------------------------------------------------------
# --- Terms & Conditions.
# -----------------------------------------------------------------------------
# @cache_page(60 * 60 * 24)
class PrivacyPolicyViewSet(TemplateView):
    """Privacy Policy Page View Set."""

    template_name = "home/privacy-policy.html"

    def get(self, request, *args, **kwrags):
        """GET."""
        print colored("***" * 27, "green")
        print colored("*** INSIDE `{}.{}`".format(
            self.__class__.__name__,
            inspect.stack()[0][3]
            ), "green")

        return self.render_to_response({})


# @cache_page(60 * 60 * 24)
class UserAgreementViewSet(TemplateView):
    """User Agreement Page View Set."""

    template_name = "home/user-agreement.html"

    def get(self, request, *args, **kwrags):
        """GET."""
        print colored("***" * 27, "green")
        print colored("*** INSIDE `{}.{}`".format(
            self.__class__.__name__,
            inspect.stack()[0][3]
            ), "green")

        return self.render_to_response({})
