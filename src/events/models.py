from django.db import models
from django.utils.translation import ugettext_lazy as _

from ddcore.models import BaseModel

from events.choices import(
    Status, STATUS_CHOICES,
    Application, APPLICATION_CHOICES,
    )


# =============================================================================
# ===
# === EVENT CATEGORY
# ===
# =============================================================================


# =============================================================================
# ===
# === EVENT
# ===
# =============================================================================
class Event(BaseModel):
    """Event Model."""

    class Meta:
        verbose_name = _("event")
        verbose_name_plural = _("events")
        ordering = ["-created", ]

    # -------------------------------------------------------------------------
    # --- Properties.

    # -------------------------------------------------------------------------
    # --- Methods.

    # -------------------------------------------------------------------------
    # --- Static Methods.

    # -------------------------------------------------------------------------
    # --- Class Methods.
