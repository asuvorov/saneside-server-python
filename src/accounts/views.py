import inspect

from django.contrib.auth.views import LoginView
from django.core.urlresolvers import reverse
from django.http import (
    HttpResponse,
    HttpResponseRedirect,
    )
from django.shortcuts import (
    get_object_or_404,
    redirect,
    render,
    )

from termcolor import colored

from accounts.forms import LoginForm


# =============================================================================
# ===
# === REGISTRATION
# ===
# =============================================================================

# -----------------------------------------------------------------------------
# --- Log-in.
# -----------------------------------------------------------------------------
class LoginViewSet(LoginView):
    """Log-in View Set."""

    authentication_form = LoginForm
    template_name = "accounts/registration/login.html"

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

        # ---------------------------------------------------------------------
        # --- Parse Request.
        # ---------------------------------------------------------------------
        redirect_to = request.GET.get("next", "")

        print colored("[---  DUMP   ---] NEXT : {}".format(
            redirect_to,
            ), "yellow")

        # ---------------------------------------------------------------------
        # --- Prepare Form(s).
        # ---------------------------------------------------------------------
        form = self.get_form()

        if request.user.is_authenticated():
            if redirect_to:
                return HttpResponseRedirect(redirect_to)

            return HttpResponseRedirect(
                reverse("my-profile-view"))

        return render(
            request, "accounts/registration/login.html", {
                "form":     form,
                "next":     redirect_to,
            })

    # @cache_page(60 * 60)
    def post(self, request, *args, **kwargs):
        """Docstring."""
        print colored("***" * 27, "green")
        print colored("*** INSIDE `{}.{}`".format(
            self.__class__.__name__,
            inspect.stack()[0][3]
            ), "green")

        # ---------------------------------------------------------------------
        # --- Parse Request.
        # ---------------------------------------------------------------------
        redirect_to = request.GET.get("next", "")

        print colored("[---  DUMP   ---] NEXT : {}".format(
            redirect_to,
            ), "yellow")

        # ---------------------------------------------------------------------
        # --- Prepare Form(s).
        # ---------------------------------------------------------------------
        form = self.get_form()

        if form.is_valid():
            # if not redirect_to:
            #     redirect_to = settings.LOGIN_REDIRECT_URL

            data = form.cleaned_data
            user = authenticate(
                username=data["username"],
                password=data["password"],
            )

            if user:
                login(request, user)

                if data["remember_me"]:
                    request.session.set_expiry(settings.SESSION_COOKIE_AGE)
                else:
                    request.session.set_expiry(0)
                # return HttpResponseRedirect(redirect_to)

                # -------------------------------------------------------------
                # --- Track IP.
                UserLogin.objects.insert(
                    request=request)

                # -------------------------------------------------------------
                # --- Save the Log.
                papertrail.log(
                    event_type="user-logged-in",
                    message="User logged in",
                    data={
                        "ip":           ip,
                        "country":      g.country(ip),
                        "city":         g.city(ip),
                        "user":         user.email,
                        "data":         data,
                    },
                    # timestamp=timezone.now(),
                    targets={
                        "user":         user,
                        "profile":      user.profile
                    },
                    )

                if redirect_to:
                    return HttpResponseRedirect(redirect_to)

                return HttpResponseRedirect(
                    reverse("my-profile-view"))
            else:
                form.add_non_field_error(
                    _("Sorry, you have entered wrong Email or Password"))

        # ---------------------------------------------------------------------
        # --- Failed to log in
        # --- Save the Log
        papertrail.log(
            event_type="user-login-failed",
            message="user login failed",
            data={
                "form":     form_field_error_list(form),
            },
            # timestamp=timezone.now(),
            targets={},
            )
