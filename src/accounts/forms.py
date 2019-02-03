from django import forms
from django.forms.forms import NON_FIELD_ERRORS
from django.forms.utils import ErrorList
from django.utils.translation import ugettext_lazy as _


# =============================================================================
# ===
# === REGISTRATION
# ===
# =============================================================================

# -----------------------------------------------------------------------------
# --- Log-in Form.
# -----------------------------------------------------------------------------
class LoginForm(forms.Form):
    """Login Form."""

    def __init__(self, *args, **kwargs):
        """Docstring."""
        super(LoginForm, self).__init__(*args, **kwargs)

    username = forms.CharField(
        label=_("Email"),
        widget=forms.TextInput(
            attrs={
                "class":        "form-control",
                "placeholder":  _("Email"),
                "value":        "",
            }))
    password = forms.CharField(
        label=_("Password"),
        widget=forms.PasswordInput(
            attrs={
                "min_length":   6,
                "max_length":   30,
                "class":        "form-control",
                "placeholder":  _("Password"),
                "value":        "",
            }))
    remember_me = forms.BooleanField(
        label=_("Keep me logged-in on this Computer"),
        required=False,
        initial=True)

    def add_non_field_error(self, message):
        """Docstring."""
        error_list = self.errors.setdefault(NON_FIELD_ERRORS, ErrorList())
        error_list.append(message)
