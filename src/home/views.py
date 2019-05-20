import inspect

from django.shortcuts import (
    get_object_or_404,
    redirect,
    render,
    )
from django.views.decorators.cache import cache_page

from termcolor import colored


# -----------------------------------------------------------------------------
# --- Index.
# -----------------------------------------------------------------------------
# @cache_page(60 * 60)
def index(request):
    """Docstring."""
    print colored("***" * 27, "green")
    print colored("*** INSIDE `%s`" % inspect.stack()[0][3], "green")

    # g = GeoIP()
    # ip = get_client_ip(request)
    # # ip = "108.162.209.69"
    # country = g.country(ip)
    # city = g.city(ip)

    # print colored("[---  DUMP   ---] COUNTRY : %s" % country, "yellow")
    # print colored("[---  DUMP   ---] CITY    : %s" % city, "yellow")

    return render(
        request, "home/index.html", {})


# -----------------------------------------------------------------------------
# --- Terms & Conditions.
# -----------------------------------------------------------------------------
# @cache_page(60 * 60 * 24)
def privacy_policy(request):
    """Docstring."""
    print colored("***" * 27, "green")
    print colored("*** INSIDE `%s`" % inspect.stack()[0][3], "green")

    return render(
        request, "home/privacy-policy.html", {})


# @cache_page(60 * 60 * 24)
def user_agreement(request):
    """Docstring."""
    print colored("***" * 27, "green")
    print colored("*** INSIDE `%s`" % inspect.stack()[0][3], "green")

    return render(
        request, "home/user-agreement.html", {})
