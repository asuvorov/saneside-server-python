from django.utils.translation import ugettext_lazy as _

from enum import Enum


# =============================================================================
# ===
# === GENDER CHOICES
# ===
# =============================================================================
class Gender(Enum):
    """Gender Enum."""

    OTHER = 0,
    FEMALE = 1,
    MALE = 2,

gender_choices = [
    (Gender.OTHER,  _("Other")),
    (Gender.FEMALE, _("Female")),
    (Gender.MALE,   _("Male")),
]
