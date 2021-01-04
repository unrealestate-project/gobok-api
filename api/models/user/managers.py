from django.contrib.auth.base_user import BaseUserManager
from django.core.validators import validate_email


class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, email, password=None):
        validate_email(email)
        # TODO: Currently saves email name as nickname.
        #  Need to change this behavior later on
        nickname, _, _ = email.partition("@")
        user = self.model(email=self.normalize_email(email),
                          nickname=nickname)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(email, password=password)
        user.is_admin = True
        user.save(using=self._db)
        return user
