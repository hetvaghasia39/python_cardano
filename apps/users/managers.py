from django.contrib.auth.base_user import BaseUserManager


class CardanoUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.set_password(password)
        user.save(using=self._db)
        return user

    def get_queryset(self):
        """
        overriding default queryset to exclude deleted users
        """
        return super().get_queryset().exclude(is_deleted=True)


class IncludeDeletedUsers(BaseUserManager):
    """
    creating custom manager to include deleted users
    """

    def get_queryset(self):
        return super().get_queryset()
