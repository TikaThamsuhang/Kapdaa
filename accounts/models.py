from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


# ----------------------------------------------------
# Custom User Manager: Handles HOW users are created
# ----------------------------------------------------
class MyAccountManager(BaseUserManager):

    # Create a normal user
    def create_user(self, first_name, last_name, username, email, password=None):
        # Email is required
        if not email:
            raise ValueError('User must have an email address')
        
        # Username is required
        if not username:
            raise ValueError('User must have a username')

        # Create user object
        user = self.model(
            email=self.normalize_email(email),  # Convert email to lowercase
            first_name=first_name,
            last_name=last_name,
            username=username,
        )

        # Hash the password before saving
        user.set_password(password)

        # Save the user to the database
        user.save(using=self._db)
        return user

    # Create a superuser (admin)
    def create_superuser(self, first_name, last_name, username, email, password=None):
        # Create a normal user first
        user = self.create_user(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            username=username,
            password=password,
        )

        # Give admin permissions
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True

        # Save the superuser
        user.save(using=self._db)
        return user



# ----------------------------------------------------
# Custom User Model
# ----------------------------------------------------
class Account(AbstractBaseUser):
    # Basic user information
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=50, unique=True)

    # Auto fields
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)

    # Permission-related fields
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    # Login with email instead of username
    USERNAME_FIELD = 'email'

    # Required when creating a superuser
    REQUIRED_FIELDS = ['first_name', 'last_name', 'username']

    # Use custom manager for creating users and superusers
    objects = MyAccountManager()

    # Display user by email
    def __str__(self):
        return self.email

    # Permission checks
    def has_perm(self, perm, obj=None):
        return self.is_admin  # Only admin has full permissions
    
    def has_module_perms(self, app_label):
        return True  # Allow access to all apps
