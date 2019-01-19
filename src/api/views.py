import inspect
import os
import re

from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from rest_framework import (
    mixins,
    parsers,
    renderers,
    status,
    views,
    viewsets,
    )
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import (
    AllowAny,
    IsAdminUser,
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
    )
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView

from termcolor import colored


# =============================================================================
# =============================================================================
# ===
# === STATUS
# ===
# =============================================================================
# =============================================================================
class APIStatusViewSet(APIView):
    """API Status View Set.

    Returns the Platform Status.

    Methods
    -------
    get()

    """

    # authentication_classes = (CsrfExemptSessionAuthentication, )
    permission_classes = (AllowAny, )
    renderer_classes = (JSONRenderer, )
    # serializer_class =
    # model =

    def get(self, request):
        """GET: Status.

        Parameters
        ----------
        request : obj

        """
        print colored("***" * 27, "green")
        print colored("*** INSIDE `{}.{}`".format(
            self.__class__.__name__,
            inspect.stack()[0][3]
            ), "green")

        # ---------------------------------------------------------------------
        # --- Initials.
        # ---------------------------------------------------------------------

        # ---------------------------------------------------------------------
        # --- Retrieve Data from the Request.
        # ---------------------------------------------------------------------

        # ---------------------------------------------------------------------
        # --- Handle Errors.
        # ---------------------------------------------------------------------

        # ---------------------------------------------------------------------
        # --- Prepare the Response.
        # ---------------------------------------------------------------------

        # ---------------------------------------------------------------------
        # --- Send the Response.
        # ---------------------------------------------------------------------
        return Response({
            "message":  _("OK"),
            "code":     status.HTTP_200_OK,
            "response": {},
        }, status=status.HTTP_200_OK)

api_status = APIStatusViewSet.as_view()


# =============================================================================
# =============================================================================
# ===
# === VERSION
# ===
# =============================================================================
# =============================================================================
class APIVersionViewSet(APIView):
    """API Version View Set.

    Returns the Platform Version.

    Methods
    -------
    get()

    """

    # authentication_classes = (CsrfExemptSessionAuthentication, )
    permission_classes = (AllowAny, )
    renderer_classes = (JSONRenderer, )
    # serializer_class =
    # model =

    def get(self, request):
        """GET: Version.

        Parameters
        ----------
        request : obj

        """
        print colored("***" * 27, "green")
        print colored("*** INSIDE `{}.{}`".format(
            self.__class__.__name__,
            inspect.stack()[0][3]
            ), "green")

        # ---------------------------------------------------------------------
        # --- Initials.
        # ---------------------------------------------------------------------

        # ---------------------------------------------------------------------
        # --- Retrieve Data from the Request.
        # ---------------------------------------------------------------------

        # ---------------------------------------------------------------------
        # --- Handle Errors.
        # ---------------------------------------------------------------------

        # ---------------------------------------------------------------------
        # --- Prepare the Response.
        # ---------------------------------------------------------------------
        PROJECT_PATH = settings.PROJECT_PATH
        VERSION_RE = re.compile(r"""__version__ = [""]([0-9.]+((dev|rc|b)[0-9]+)?)[""]""")
        VERSION = ""

        file_abspath = os.path.abspath(
            os.path.join(
                PROJECT_PATH,
                "__init__.py"))

        with open(file_abspath, "r") as init_file:
            init = init_file.read()

            VERSION = VERSION_RE.search(init).group(1)

        # ---------------------------------------------------------------------
        # --- Send the Response.
        # ---------------------------------------------------------------------
        return Response({
            "message":  _("success"),
            "code":     status.HTTP_200_OK,
            "response": {
                "version":  VERSION,
            },
        }, status=status.HTTP_200_OK)

api_version = APIVersionViewSet.as_view()
