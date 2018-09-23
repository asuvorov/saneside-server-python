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
        # print colored("***" * 27, "green")
        # print colored("*** INSIDE `%s.%s`" % (self.__class__.__name__, inspect.stack()[0][3]), "green")

        # ---------------------------------------------------------------------
        # --- Retrieve Data from the Request.
        # ---------------------------------------------------------------------

        # ---------------------------------------------------------------------
        # --- Handle Errors.
        # ---------------------------------------------------------------------

        # ---------------------------------------------------------------------
        # --- Send the Response.
        return Response({
            "message":      _("Successfully sent the Password Renewal Link."),
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
        # print colored("***" * 27, "green")
        # print colored("*** INSIDE `%s.%s`" % (self.__class__.__name__, inspect.stack()[0][3]), "green")

        # ---------------------------------------------------------------------
        # --- Retrieve Data from the Request.
        # ---------------------------------------------------------------------

        # ---------------------------------------------------------------------
        # --- Handle Errors.
        # ---------------------------------------------------------------------

        # ---------------------------------------------------------------------
        # --- Send the Response.
        return Response({
            "message":      _("Successfully sent the Password Renewal Link."),
        }, status=status.HTTP_200_OK)

api_version = APIVersionViewSet.as_view()
