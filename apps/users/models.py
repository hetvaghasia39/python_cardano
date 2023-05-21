import binascii
import os

from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models

from apps.users.managers import CardanoUserManager, IncludeDeletedUsers


class CardanoUser(AbstractBaseUser):
    """
    Default User table for project
    """

    username = models.CharField(max_length=256)
    password = models.CharField(max_length=256)
    email = models.EmailField(max_length=256, unique=True)
    is_deleted = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["password"]

    objects = CardanoUserManager()
    include_deleted_users = IncludeDeletedUsers()

    def __unicode__(self):
        return "%s" % self.username

    def get_full_name(self):
        return self.username

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        return True

    def mark_deleted(self):
        """
        soft delete user
        """
        self.is_deleted = True
        self.is_active = False
        self.save()


class Token(models.Model):
    """
    The default authorization token model.
    """

    key = models.CharField("Key", max_length=40, primary_key=True)
    user = models.ForeignKey(
        CardanoUser, verbose_name="User", related_name="tokens", on_delete=models.CASCADE
    )

    device_token = models.CharField(max_length=256, null=True, blank=True)
    device_id = models.CharField(max_length=256, null=False, blank=False)
    device_type = models.CharField(max_length=64, null=True, blank=True)
    created_at = models.DateTimeField("created", auto_now_add=True)

    class Meta:
        verbose_name = "Token"
        verbose_name_plural = "Tokens"
        ordering = ("-created_at",)

    def save(self, *args, **kwargs):
        if not self.key:
            self.key = self.generate_key()
        return super(Token, self).save(*args, **kwargs)

    def generate_key(self):
        return binascii.hexlify(os.urandom(20)).decode()

    def __str__(self):
        return self.key
