from django import forms
from django.forms.forms import NON_FIELD_ERRORS
from django.forms.utils import ErrorList
from django.utils.translation import ugettext_lazy as _

from annoying.functions import get_object_or_None
from captcha.fields import CaptchaField
from passwords.fields import PasswordField

from accounts.models import User


# -----------------------------------------------------------------------------
# --- USER FORM
# -----------------------------------------------------------------------------
class UserForm(forms.ModelForm):
    """User Form."""

    def __init__(self, *args, **kwargs):
        """Docstring."""
        super(UserForm, self).__init__(*args, **kwargs)

        if self.instance and self.instance.id:
            pass

        # self.fields["username"].required = False
        self.fields["first_name"].required = True
        self.fields["last_name"].required = True
        self.fields["email"].required = True

    password = PasswordField(
        label=_("Password"),
        widget=forms.PasswordInput(
            attrs={
                "min_length":   6,
                "max_length":   30,
                "class":        "form-control",
                "placeholder":  _("Password"),
                "value":        "",
            }))
    retry = forms.CharField(
        widget=forms.PasswordInput(
            render_value=True,
            attrs={
                "min_length":   6,
                "max_length":   30,
                "class":        "form-control",
                "placeholder":  _("Retry"),
                "value":        "",
            }))
    captcha = CaptchaField()
    birthday = forms.DateField(
        input_formats=("%m/%d/%Y",),
        widget=forms.DateInput(
            format="%m/%d/%Y",
            attrs={
                "class":    "form-control",
            }))

    class Meta:
        model = User
        fields = [
            "first_name", "last_name", "email", "password",
            "avatar", "nickname", "bio", "gender", "birthday",
            "receive_newsletters",
        ]
        widgets = {
            "first_name": forms.TextInput(
                attrs={
                    "class":        "form-control",
                    "placeholder":  _("First Name"),
                    "maxlength":    30,
                }),
            "last_name": forms.TextInput(
                attrs={
                    "class":        "form-control",
                    "placeholder":  _("Last Name"),
                    "maxlength":    30,
                }),
            "email": forms.EmailInput(
                attrs={
                    "class":        "form-control",
                    "placeholder":  _("Email"),
                }),
            "nickname": forms.TextInput(
                attrs={
                    "class":        "form-control",
                    "placeholder":  _("Nickname"),
                    "maxlength":    30,
                }),
            "bio": forms.Textarea(
                attrs={
                    "class":        "form-control",
                    "placeholder":  _("Tell us a bit about yourself."),
                    "maxlength":    1000,
                }),
            "gender": forms.Select(
                attrs={
                    "class":        "form-control selectpicker",
                }),
            "birthday": forms.DateInput(
                attrs={
                    "class":        "form-control",
                }),
            }

    def clean_email(self):
        """Docstring."""
        user = get_object_or_None(
            User,
            email=self.cleaned_data.get("email", "")
            )

        if user:
            raise forms.ValidationError(
                _("User already exists."))

        return self.cleaned_data["email"]

    def clean_retry(self):
        """Docstring."""
        if self.cleaned_data["retry"] != self.cleaned_data.get("password", ""):
            raise forms.ValidationError(
                _("Passwords don't match."))

        return self.cleaned_data["retry"]

    def save(self, commit=True):
        """Docstring."""
        instance = super(UserForm, self).save(commit=False)
        instance.username = self.cleaned_data["email"]

        if commit:
            instance.save()

        return instance
