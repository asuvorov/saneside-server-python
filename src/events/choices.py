from django.utils.translation import ugettext_lazy as _

from enum import Enum


# =============================================================================
# ===
# === EVENT CHOICES
# ===
# =============================================================================
class Status(Enum):
    """Event Status Enum."""

    DRAFT = 0
    UPCOMING = 1
    COMPLETE = 2
    EXPIRED = 3
    CLOSED = 4

STATUS_CHOICES = [
    (Status.DRAFT,    _("Draft")),
    (Status.UPCOMING, _("Upcoming")),
    (Status.COMPLETE, _("Complete")),
    (Status.EXPIRED,  _("Expired")),
    (Status.CLOSED,   _("Closed")),
]


class Application(Enum):
    """Event Application Enum."""

    FREE_FOR_ALL = 0
    CONFIRMATION_REQUIRED = 1

APPLICATION_CHOICES = [
    (Application.FREE_FOR_ALL,
        _("Anyone can participate.")),
    (Application.CONFIRMATION_REQUIRED,
        _("Participate only after a confirmed Application.")),
]


# =============================================================================
# ===
# === EVENT CATEGORY CHOICES
# ===
# =============================================================================
class Category(Enum):
    """Event Category Choices."""

    ANIMALS = 0
    ARTS = 1
    YOUTH = 2
    COMMUNITY = 3
    EDUCATION = 4
    ENVIRONMENT = 5
    HEALTH = 6
    RECREATION = 7
    SENIOURS = 8

CATEGORY_CHOICES = [
    (Category.ANIMALS,      _("Animals")),
    (Category.ARTS,         _("Arts & Culture")),
    (Category.YOUTH,        _("Children & Youth")),
    (Category.COMMUNITY,    _("Community")),
    (Category.EDUCATION,    _("Education & Literacy")),
    (Category.ENVIRONMENT,  _("Environment")),
    (Category.HEALTH,       _("Health & Wellness")),
    (Category.RECREATION,   _("Sports & Recreation")),
    (Category.SENIOURS,     _("Veterans & Seniors")),
]

class CategoryColor(Enum):
    """Event Category Colors Choices."""

    ANIMALS = 0
    ARTS = 1
    YOUTH = 2
    COMMUNITY = 3
    EDUCATION = 4
    ENVIRONMENT = 5
    HEALTH = 6
    RECREATION = 7
    SENIOURS = 8

CATEGORY_COLOR_CHOICES = [
    (CategoryColor.ANIMALS,     "DarkKhaki"),
    (CategoryColor.ARTS,        "LightSteelBlue"),
    (CategoryColor.YOUTH,       "SlateBlue"),
    (CategoryColor.COMMUNITY,   "DarkOrange"),
    (CategoryColor.EDUCATION,   "#DEB887"),
    (CategoryColor.ENVIRONMENT, "Green"),
    (CategoryColor.HEALTH,      "Red"),
    (CategoryColor.RECREATION,  "LightSeaGreen"),
    (CategoryColor.SENIOURS,    "SaddleBrown"),
]


class CategoryIcon(Enum):
    """Event Category Icon Choices."""
    ANIMALS = 0
    ARTS = 1
    YOUTH = 2
    COMMUNITY = 3
    EDUCATION = 4
    ENVIRONMENT = 5
    HEALTH = 6
    RECREATION = 7
    SENIOURS = 8

CATEGORY_ICON_CHOICES = [
    (CategoryIcon.ANIMALS,      "fa fa-paw fa-fw"),
    (CategoryIcon.ARTS,         "fa fa-wrench fa-fw"),
    (CategoryIcon.YOUTH,        "fa fa-child fa-fw"),
    (CategoryIcon.COMMUNITY,    "fa fa-users fa-fw"),
    (CategoryIcon.EDUCATION,    "fa fa-book fa-fw"),
    (CategoryIcon.ENVIRONMENT,  "fa fa-tree fa-fw"),
    (CategoryIcon.HEALTH,       "fa fa-heartbeat fa-fw"),
    (CategoryIcon.RECREATION,   "fa fa-bicycle fa-fw"),
    (CategoryIcon.SENIOURS,     "fa fa-home fa-fw"),
]


class CategoryImage(Enum):
    """Event Category Image Choices."""

    ANIMALS = 0
    ARTS = 1
    YOUTH = 2
    COMMUNITY = 3
    EDUCATION = 4
    ENVIRONMENT = 5
    HEALTH = 6
    RECREATION = 7
    SENIOURS = 8

CATEGORY_IMAGE_CHOICES = [
    (CategoryImage.ANIMALS,     "/img/challenge-categories/1-animals.jpeg"),
    (CategoryImage.ARTS,        "/img/challenge-categories/2-arts-and-culture.jpeg"),
    (CategoryImage.YOUTH,       "/img/challenge-categories/3-children-and-youth.jpeg"),
    (CategoryImage.COMMUNITY,   "/img/challenge-categories/4-community.jpeg"),
    (CategoryImage.EDUCATION,   "/img/challenge-categories/5-education-and-literacy.jpeg"),
    (CategoryImage.ENVIRONMENT, "/img/challenge-categories/6-environment-2.jpeg"),
    (CategoryImage.HEALTH,      "/img/challenge-categories/7-health-and-wellness.jpeg"),
    (CategoryImage.RECREATION,  "/img/challenge-categories/8-sports-and-recreation.jpeg"),
    (CategoryImage.SENIOURS,    "/img/challenge-categories/9-veterans-and-seniors.jpeg"),
]


# =============================================================================
# ===
# === EVENT TYPE CHOICES
# ===
# =============================================================================
class Type(Enum):
    """Event Type Choices."""

    CHALLENGE = 0
    FAMILY_EVENT = 1
    SPORTS_EVENT = 2
    CONFERENCE = 3
    MEET_UP = 4
    ANNIVERSARY = 5
    WEDDING = 6
    THEME_PARTY = 7
    FESTIVAL = 8
    CHARITABLE_AUCTION = 9
    HAPPY_HOUR = 10
    RETREAT = 11

CATEGORY_CHOICES = [
    (Type.CHALLENGE,            _("Challenge")),
    (Type.FAMILY_EVENT,         _("Family Event")),
    (Type.SPORTS_EVENT,         _("Sports Event")),
    (Type.CONFERENCE,           _("Conference")),
    (Type.MEET_UP,              _("Meet up")),
    (Type.ANNIVERSARY,          _("Anniversary")),
    (Type.WEDDING,              _("Wedding")),
    (Type.THEME_PARTY,          _("Theme Party")),
    (Type.FESTIVAL,             _("Festival")),
    (Type.CHARITABLE_AUCTION,   _("Charitable Auction")),
    (Type.HAPPY_HOUR,           _("Happy Hour")),
    (Type.RETREAT,              _("Retreat")),
]


# =============================================================================
# ===
# === EVENT PARTICIPATION CHOICES
# ===
# =============================================================================
class ParticipationRemoveMode(Enum):
    """Event Participation remove Mode Choices."""

    REMOVE_APPLICATION = 0
    REJECT_APPLICATION = 1
    REJECT_SELFREFLECTION = 2
    ACKNOWLEDGE = 3


class ParticipationStatus(Enum):
    """Event Participation Status Choices."""

    WAITING_FOR_CONFIRMATION = 0
    CONFIRMATION_DENIED = 1
    CONFIRMED = 2
    CANCELLED_BY_ADMIN = 3
    CANCELLED_BY_USER = 4
    WAITING_FOR_SELFREFLECTION = 5
    WAITING_FOR_ACKNOWLEDGEMENT = 6
    ACKNOWLEDGED = 7

PARTICIPATION_STATUS_CHOICES = [
    (ParticipationStatus.WAITING_FOR_CONFIRMATION,
        _("Waiting for Confirmation")),
    (ParticipationStatus.CONFIRMATION_DENIED,
        _("You were not accepted to this Challenge")),
    (ParticipationStatus.CONFIRMED,
        _("Signed up")),
    (ParticipationStatus.CANCELLED_BY_ADMIN,
        _("The Organizer removed you from this Challenge")),
    (ParticipationStatus.CANCELLED_BY_USER,
        _("You withdrew your Participation to this Challenge")),
    (ParticipationStatus.WAITING_FOR_SELFREFLECTION,
        _("Please, write your Experience Report")),
    (ParticipationStatus.WAITING_FOR_ACKNOWLEDGEMENT,
        _("Waiting for Acknowledgment")),
    (ParticipationStatus.ACKNOWLEDGED,
        _("Report acknowledged")),
]


# =============================================================================
# ===
# === EVENT RECURRENCE CHOICES
# ===
# =============================================================================
