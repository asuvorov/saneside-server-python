import inspect

from django.views.generic import TemplateView
from django.shortcuts import (
    get_object_or_404,
    redirect,
    render,
    )
# from django.views.decorators.cache import cache_page

from termcolor import colored


# -----------------------------------------------------------------------------
# --- Index.
# -----------------------------------------------------------------------------
class IndexViewSet(TemplateView):
    """Index View Set."""

    # @cache_page(60 * 60)
    def get(self, request, *args, **kwargs):
        """Docstring."""
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

        timeline_qs = []
        # timeline_qs = sorted(
        #     chain(
        #         Post.objects.all(),
        #         Challenge.objects.get_upcoming(),
        #         Organization.objects.filter(
        #             is_hidden=False,
        #             is_deleted=False,
        #         )
        #     ),
        #     key=attrgetter("created"))[:10]

        return render(
            request, "home/index.html", {
                "timeline_qs":  timeline_qs,
            })


# -----------------------------------------------------------------------------
# --- Privacy Policy.
# -----------------------------------------------------------------------------
class PrivacyPolicyViewSet(TemplateView):
    """Privacy Policy View Set."""

    # @cache_page(60 * 60)
    def get(self, request, *args, **kwargs):
        """Docstring."""
        print colored("***" * 27, "green")
        print colored("*** INSIDE `{}.{}`".format(
            self.__class__.__name__,
            inspect.stack()[0][3]
            ), "green")

        return render(
            request, "home/privacy-policy.html", {})


# -----------------------------------------------------------------------------
# --- Privacy Policy.
# -----------------------------------------------------------------------------
class UserAgreementViewSet(TemplateView):
    """User Agreement View Set."""

    # @cache_page(60 * 60)
    def get(self, request, *args, **kwargs):
        """Docstring."""
        print colored("***" * 27, "green")
        print colored("*** INSIDE `{}.{}`".format(
            self.__class__.__name__,
            inspect.stack()[0][3]
            ), "green")

        return render(
            request, "home/user-agreement.html", {})
