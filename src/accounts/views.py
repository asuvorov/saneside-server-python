import inspect

from django.conf import settings
from django.contrib.auth import (
    authenticate,
    login,
    )
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.tokens import (
    default_token_generator as token_generator
    )
from django.contrib.auth.views import (
    auth_login,
    logout,
    )
from django.contrib.contenttypes.models import ContentType
from django.contrib.gis.geoip import GeoIP
from django.core.paginator import (
    EmptyPage,
    PageNotAnInteger,
    Paginator,
    )
from django.core.urlresolvers import reverse
from django.db.models import Q
from django.http import (
    HttpResponse,
    HttpResponseRedirect,
    )
from django.shortcuts import (
    get_object_or_404,
    render,
    )
from django.utils.http import (
    base36_to_int,
    int_to_base36,
    )
from django.utils.translation import ugettext as _
from django.views.decorators.cache import cache_page
from django.views.decorators.csrf import csrf_exempt

from termcolor import colored

from accounts.forms import UserForm


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~
# ~~~ DESKTOP
# ~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# -----------------------------------------------------------------------------
# --- ACCOUNT REGISTRATION
# -----------------------------------------------------------------------------
def account_signup(request):
    """Sign up."""
    print colored("***" * 27, "green")
    print colored("*** INSIDE `{}`".format(
        inspect.stack()[0][3],
        ), "green")

    # g = GeoIP()
    # ip = get_client_ip(request)
    # country_code = g.country_code(ip)

    # -------------------------------------------------------------------------
    # --- Prepare Form(s).
    # -------------------------------------------------------------------------
    uform = UserForm(
        request.POST or None, request.FILES or None)
    """
    aform = AddressForm(
        request.POST or None, request.FILES or None,
        country_code=country_code)
    nform = PhoneForm(
        request.POST or None, request.FILES or None)
    """

    if request.method == "GET":
        if request.user.is_authenticated():
            return HttpResponseRedirect(
                reverse("my-profile-view"))

    if request.method == "POST":
        # if (
        #         uform.is_valid() and pform.is_valid() and
        #         aform.is_valid() and nform.is_valid()):
        if uform.is_valid():
            # -----------------------------------------------------------------
            # --- Create User.
            user = uform.save(commit=False)
            user.is_active = False
            user.save()
            user.set_password(uform.cleaned_data["password"])
            user.save()

            # -----------------------------------------------------------------
            # --- Create User Privacy.
            UserPrivacyGeneral.objects.create(
                user=user)
            UserPrivacyMembers.objects.create(
                user=user)
            UserPrivacyAdmins.objects.create(
                user=user)

            """
            user.backend = "django.contrib.auth.backends.ModelBackend"
            auth_login(request, user)

            return HttpResponseRedirect(reverse("index"))
            """

            uidb36 = int_to_base36(user.id)
            token = token_generator.make_token(user)

            DOMAIN_NAME = request.get_host()
            url = reverse(
                "signup-confirm", kwargs={
                    "uidb36":   uidb36,
                    "token":    token,
                })
            confirmation_link = "http://{domain}{url}".format(
                domain=DOMAIN_NAME,
                url=url,
                )

            # -----------------------------------------------------------------
            # --- Send Email Notification(s).
            user.email_notify_signup_confirmation(
                request=request,
                url=confirmation_link)

            # -----------------------------------------------------------------
            # --- Save the Log.
            # papertrail.log(
            #     event_type="new-user-signed-up",
            #     message="New User has signed up",
            #     data={
            #         "user":         user.email,
            #     },
            #     # timestamp=timezone.now(),
            #     targets={
            #         "user":         user,
            #         "profile":      profile,
            #     },
            #     )

            # -----------------------------------------------------------------
            # --- Save the Log.
            # papertrail.log(
            #     event_type="user-sign-up-submitted",
            #     message="User sign up submitted",
            #     data={
            #         "ip":           ip,
            #         "country":      g.country(ip),
            #         "city":         g.city(ip),
            #         "uform":        form_field_error_list(uform),
            #         "pform":        form_field_error_list(pform),
            #         # "aform":        form_field_error_list(aform),
            #         # "nform":        form_field_error_list(nform),
            #     },
            #     # timestamp=timezone.now(),
            #     targets={},
            #     )

            return render(
                request,
                "accounts/account-signup-confirmation-email-sent.html", {
                    "email":    user.email,
                })

        # ---------------------------------------------------------------------
        # --- Failed to sign up.
        # --- Save the Log.
        # papertrail.log(
        #     event_type="user-sign-up-failed",
        #     message="User sign up failed",
        #     data={
        #         "ip":           ip,
        #         "country":      g.country(ip),
        #         "city":         g.city(ip),
        #         "uform":        form_field_error_list(uform),
        #         "pform":        form_field_error_list(pform),
        #         # "aform":        form_field_error_list(aform),
        #         # "nform":        form_field_error_list(nform),
        #     },
        #     # timestamp=timezone.now(),
        #     targets={},
        #     )

    return render(
        # request, "accounts/account_signup_all.html", {
        request, "accounts/account-signup.html", {
            "uform":    uform,
            # "aform":    aform,
            # "nform":    nform,
        })
