from django.utils.translation import ugettext_lazy as _

from enum import Enum


# =============================================================================
# ===
# === GENDER CHOICES
# ===
# =============================================================================
class Gender(Enum):
    """Gender Enum."""

    OTHER = "other"
    FEMALE = "female"
    MALE = "male"


gender_choices = [
    (Gender.OTHER,  _("Other")),
    (Gender.FEMALE, _("Female")),
    (Gender.MALE,   _("Male")),
]
