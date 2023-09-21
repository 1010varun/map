from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models


class CustomUserManager(BaseUserManager):
    def create_user(self, agencyID, password=None, **extra_fields):
        if not agencyID:
            raise ValueError('The agencyID field must be set')
        user = self.model(agencyID=agencyID, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, agencyID, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(agencyID, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    agencyID = models.CharField(unique=True, max_length=100)
    agencyName = models.CharField(max_length=100)
    type = models.CharField(max_length=100, default="Type of agency")
    frequency = models.FloatField(default=0.0)
    resources = models.CharField(max_length=100, default="Resources of agency")
    SOPs = models.CharField(max_length=256, default="SOPs of agency")
    emergencyplan = models.CharField(max_length=256, default="Emergency Plan of agency")
    latitude = models.FloatField(null=True, default=0.000)
    longitude = models.FloatField(null=True, default=0.000)
    is_verified = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'agencyID'
    REQUIRED_FIELDS = ['type', 'frequency', 'resources']

    def __str__(self):
        return self.agencyID