from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _

from ddcore.models import BaseModel

from accounts.choices import (
    Gender, gender_choices)


# =============================================================================
# ===
# === USER PROFILE
# ===
# =============================================================================
def user_directory_path(instance, filename):
    """User Directory Path.

    File will be uploaded to MEDIA_ROOT/accounts/<id>/avatars/<filename>.
    """

    return "accounts/{id}/avatars/{fname}".format(
        id=instance.user.id,
        fname=get_unique_filename(
            filename.split("/")[-1]
            ))


class User(AbstractUser, BaseModel):
    """User Model.

    Attributes
    ----------
    username : str
        User Name
    first_name : str, optional
        First Name.
    last_name : str, optional
        Last Name.
    email : str, optional
        Email.

    avatar: obj, optional
        User Avatar.
    nickname: obj, optional
        User Nickname.
    bio: obj, optional
        User Biography.
    gender: obj, optional
        User Gender.
    birthday: obj, optional
        User Birthday.
    address: obj, optional
        FK to Address Object.
    phone_number: obj, optional
        FK to Phone Object.
    receive_newsletters: obj, optional
        Flag.
    is_newly_created: obj
        Flag.

    Properties
    ----------

    Methods
    -------

    Static Methods
    --------------

    Class Methods
    -------------

    Signals
    -------

    """

    # -------------------------------------------------------------------------
    # --- Basics
    avatar = models.ImageField(
        upload_to=user_directory_path,
        blank=True)
    nickname = models.CharField(
        db_index=True,
        max_length=32, null=True, blank=True,
        default="",
        verbose_name=_("Nickname"),
        help_text=_("User Nickname"))
    bio = models.TextField(
        null=True, blank=True,
        default="",
        verbose_name="Bio",
        help_text=_("User Bio"))

    gender = models.CharField(
        max_length=8,
        choices=gender_choices,
        default=Gender.OTHER.value,
        verbose_name=_("Gender"),
        help_text=_("User Gender"))
    birthday = models.DateField(
        db_index=True,
        null=True, blank=True,
        verbose_name=_("Birthday"),
        help_text=_("User Birthday"))

    # -------------------------------------------------------------------------
    # --- Address & Phone Number.
    # address = models.ForeignKey(
    #     Address,
    #     db_index=True,
    #     null=True, blank=True,
    #     verbose_name=_("Address"),
    #     help_text=_("User Address"))
    # phone_number = models.ForeignKey(
    #     Phone,
    #     db_index=True,
    #     null=True, blank=True,
    #     verbose_name=_("Phone Numbers"),
    #     help_text=_("User Phone Numbers"))

    # -------------------------------------------------------------------------
    # --- Flags.
    receive_newsletters = models.BooleanField(
        default=False,
        verbose_name=_("I would like to receive Email Updates"),
        help_text=_("I would like to receive Email Updates"))

    is_newly_created = models.BooleanField(
        default=True)

    USERNAME_FIELD = "username"
    # REQUIRED_FIELDS = ["username", ]

    class Meta:
        """Meta Class."""
        verbose_name = _("user")
        verbose_name_plural = _("users")
        ordering = [
            "user__first_name",
            "user__last_name",
        ]

    def __repr__(self):
        """Docstring."""
        return u"<{} ({}: '{}')>".format(
            self.__class__.__name__,
            self.id,
            self.email)

    def __unicode__(self):
        """Docstring."""
        return u"{}".format(
            self.email)

    def __str__(self):
        """Docstring."""
        return self.__unicode__()

    # -------------------------------------------------------------------------
    # --- Profile direct URL.
    # -------------------------------------------------------------------------
    def public_url(self, request=None):
        """Docstring."""
        if request:
            DOMAIN_NAME = request.get_host()
        else:
            DOMAIN_NAME = settings.DOMAIN_NAME

        url = reverse(
            "profile-view", kwargs={
                "user_id":  self.user_id,
            })
        profile_link = u"http://{domain}{url}".format(
            domain=DOMAIN_NAME,
            url=url,
            )

        return profile_link

    def get_absolute_url(self):
        """Method to be called by Django Sitemap Framework."""
        url = reverse(
            "profile-view", kwargs={
                "user_id":  self.user_id,
            })

        return url

    # -------------------------------------------------------------------------
    # --- Properties.
    # -------------------------------------------------------------------------
    # @property
    # def grace_period_days_left(self):
    #     """Docstring."""
    #     dt = pendulum.today() - self.created

    #     if dt.days >= settings.PROFILE_COMPLETENESS_GRACE_PERIOD:
    #         return 0

    #     return settings.PROFILE_COMPLETENESS_GRACE_PERIOD - dt.days

    @property
    def is_completed(self):
        """Docstring."""
        return self.completeness_total >= 80 or self.grace_period_days_left > 0

    @property
    def completeness_total(self):
        """Return Profile Completeness."""
        completeness_user = (
            int(bool(self.user.username)) +
            int(bool(self.user.first_name)) +
            int(bool(self.user.last_name)) +
            int(bool(self.user.email))
        )

        completeness_profile = (
            int(bool(self.avatar)) +
            int(bool(self.nickname)) +
            int(bool(self.bio)) +
            int(bool(self.gender)) +
            int(bool(self.birth_day))
        )

        completeness_address = 0
        if self.address:
            completeness_address = (
                int(bool(self.address.address_1)) +
                int(bool(self.address.city)) +
                int(bool(self.address.zip_code)) +
                int(bool(self.address.province)) +
                int(bool(self.address.country))
            )

        completeness_phone = 0
        if self.phone_number:
            completeness_phone = (
                int(bool(self.phone_number.phone_number)) +
                int(bool(self.phone_number.mobile_phone_number))
            )

        completeness_total = int(((
            completeness_user +
            completeness_profile +
            completeness_address +
            completeness_phone
        ) / 16.0) * 100)

        return completeness_total

    @property
    def stat_gender_name(self):
        """Docstring."""
        for code, name in gender_choices:
            if self.gender == code:
                return name.lower()

        return ""

    @property
    def full_name_straight(self):
        """Docstring."""
        return self.user.first_name + " " + self.user.last_name

    @property
    def full_name(self):
        """Docstring."""
        return self.user.last_name + ", " + self.user.first_name

    @property
    def short_name(self):
        """Docstring."""
        try:
            return self.user.first_name + " " + self.user.last_name[0] + "."
        except Exception as e:
            print colored("###" * 27, "white", "on_red")
            print colored("### EXCEPTION @ `{module}`: {msg}".format(
                module=inspect.stack()[0][3],
                msg=str(e),
                ), "white", "on_red")

            return self.user.first_name

    @property
    def auth_name(self):
        """Docstring."""
        try:
            if self.short_name:
                return self.short_name
            elif self.nickname:
                return self.nickname
            else:
                return self.user.email.split("@")[0]
        except:
            pass

        return "------"

    @property
    def name(self):
        """Docstring."""
        return self.user.get_full_name()

    # -------------------------------------------------------------------------
    # --- Methods.
    # -------------------------------------------------------------------------
    def email_notify_signup_confirmation(self, request=None, url=None):
        """Send Notification to the User."""
        print colored("***" * 27, "green")
        print colored("*** INSIDE `%s`" % inspect.stack()[0][3], "green")

        # ---------------------------------------------------------------------
        # --- Render HTML Email Content.
        greetings = _(
            "Dear, %(name)s.") % {
                "name":     self.user.first_name,
            }
        htmlbody = _(
            "<p>To finish your registration Process, please, follow this \"<a href=\"%(confirmation_link)s\">Link</a>\".</p>") % {
                "confirmation_link":    url,
            }

        # ---------------------------------------------------------------------
        # --- Send Email
        send_templated_email(
            template_subj={
                "name":     "accounts/emails/account_signup_confirmation_subject.txt",
                "context":  {},
            },
            template_text={
                "name":     "accounts/emails/account_signup_confirmation.txt",
                "context":  {
                    "user":                 self.user,
                    "confirmation_link":    url,
                },
            },
            template_html={
                "name":     "emails/base.html",
                "context":  {
                    "greetings":    greetings,
                    "htmlbody":     htmlbody,
                },
            },
            from_email=settings.EMAIL_SENDER,
            to=[
                self.user.email,
            ],
            headers=None,
        )

    def email_notify_signup_confirmed(self, request=None, url=None):
        """Send Notification to the User."""
        print colored("***" * 27, "green")
        print colored("*** INSIDE `%s`" % inspect.stack()[0][3], "green")

        # ---------------------------------------------------------------------
        # ---  Render HTML Email Content.
        greetings = _(
            "Dear, %(name)s.") % {
                "name":     self.user.first_name,
            }
        htmlbody = _(
            "<p>Your Account was successfully confirmed.</p>"
            "<p>To log-in, please, follow this \"<a href=\"%(login_link)s\">Link</a>\".</p>") % {
                "login_link":   url,
            }

        # --- Send Email.
        send_templated_email(
            template_subj={
                "name":     "accounts/emails/account_signup_confirmed_subject.txt",
                "context":  {},
            },
            template_text={
                "name":     "accounts/emails/account_signup_confirmed.txt",
                "context":  {
                    "user":         self.user,
                    "login_link":   url,
                },
            },
            template_html={
                "name":     "emails/base.html",
                "context":  {
                    "greetings":    greetings,
                    "htmlbody":     htmlbody,
                },
            },
            from_email=settings.EMAIL_SENDER,
            to=[
                self.user.email,
            ],
            headers=None,
        )

    def email_notify_password_reset(self, request=None, url=None):
        """Send Notification to the User."""
        print colored("***" * 27, "green")
        print colored("*** INSIDE `%s`" % inspect.stack()[0][3], "green")

        # ---------------------------------------------------------------------
        # ---  Render HTML Email Content.
        greetings = _(
            "Dear, %(name)s.") % {
                "name":     self.user.first_name,
            }
        htmlbody = _(
            "<p>You are about to restore your Password on SaneSide.</p>"
            "<p>To proceed, please, follow this \"<a href=\"%(confirmation_link)s\">Link</a>\".</p>") % {
                "confirmation_link":    url,
            }

        # --- Send Email.
        send_templated_email(
            template_subj={
                "name":     "accounts/emails/account_forgot_password_notify_subject.txt",
                "context":  {},
            },
            template_text={
                "name":     "accounts/emails/account_forgot_password_notify.txt",
                "context":  {
                    "user":                 self.user,
                    "confirmation_link":    url,
                },
            },
            template_html={
                "name":     "emails/base.html",
                "context":  {
                    "greetings":    greetings,
                    "htmlbody":     htmlbody,
                },
            },
            from_email=settings.EMAIL_SENDER,
            to=[
                self.user.email,
            ],
            headers=None,
        )

    def email_notify_password_changed(self, request=None, url=None):
        """Send Notification to the User."""
        print colored("***" * 27, "green")
        print colored("*** INSIDE `%s`" % inspect.stack()[0][3], "green")

        # ---------------------------------------------------------------------
        # --- Render HTML Email Content.
        greetings = _(
            "Dear, %(name)s.") % {
                "name":     request.user.first_name,
            }
        htmlbody = _(
            "<p>You have successfully reset the Password from your Account.</p>"
            "<p>To log-in, please, follow this \"<a href=\"%(login_link)s\">Link</a>\".</p>") % {
                "login_link":   url,
            }

        # --- Send Email.
        send_templated_email(
            template_subj={
                "name":     "accounts/emails/account_successful_password_reset_subject.txt",
                "context":  {},
            },
            template_text={
                "name":     "accounts/emails/account_successful_password_reset.txt",
                "context":  {
                    "user":         self.user,
                    "login_link":   url,
                },
            },
            template_html={
                "name":     "emails/base.html",
                "context":  {
                    "greetings":    greetings,
                    "htmlbody":     htmlbody,
                },
            },
            from_email=settings.EMAIL_SENDER,
            to=[
                self.user.email,
            ],
            headers=None,
        )

    def image_tag(self):
        """Render Avatar Thumbnail."""
        if self.avatar:
            return u"<img src='{url}' width='{width}' height='{height}' />".format(
                url=self.avatar.url,
                width=100,
                height=100,
                )

        return "(Sin Imagen)"

    image_tag.short_description = "Avatar"
    image_tag.allow_tags = True

    # -------------------------------------------------------------------------
    # --- Static Methods.
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # --- Class Methods.
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # --- Signals.
    # -------------------------------------------------------------------------
    def pre_save(self, **kwargs):
        """Docstring."""
        pass

    def post_save(self, created, **kwargs):
        """Docstring."""
        # # ---------------------------------------------------------------------
        # # --- Ping Google.
        # try:
        #     ping_google()
        # except Exception as e:
        #     print colored("###" * 27, "white", "on_red")
        #     print colored("### EXCEPTION @ `{module}`: {msg}".format(
        #         module=inspect.stack()[0][3],
        #         msg=str(e),
        #         ), "white", "on_red")

        # # ---------------------------------------------------------------------
        # # --- Update/insert SEO Model Instance Metadata.
        # update_seo_model_instance_metadata(
        #     title=self.user.get_full_name(),
        #     description=self.bio,
        #     keywords=self.nickname,
        #     heading=self.user.get_full_name(),
        #     path=self.get_absolute_url(),
        #     object_id=self.id,
        #     content_type_id=ContentType.objects.get_for_model(self).id,
        # )

        # ---------------------------------------------------------------------
        # --- The Path for uploading Avatar Images is:
        #
        #            MEDIA_ROOT/accounts/<id>/avatars/<filename>
        #
        # --- As long as the uploading Path is being generated before
        #     the Profile Instance gets assigned with the unique ID,
        #     the uploading Path for the brand new Profile looks like:
        #
        #            MEDIA_ROOT/accounts/None/avatars/<filename>
        #
        # --- To fix this:
        #     1. Open the Avatar File in the Path;
        #     2. Assign the Avatar File Content to the Profile Avatar Object;
        #     3. Save the Profile Instance. Now the Avatar Image in the
        #        correct Path;
        #     4. Delete previous Avatar File;
        #
        try:
            if created:
                avatar = File(storage.open(self.avatar.file.name, "rb"))

                self.avatar = avatar
                self.save()

                storage.delete(avatar.file.name)
        except:
            pass

    def pre_delete(self, **kwargs):
        """Docstring."""
        pass

    def post_delete(self, **kwargs):
        """Docstring."""
        pass
