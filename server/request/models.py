from django.db import models
from authUser.models import *

class agencyNotification(models.Model):
    agency = models.ForeignKey(CustomUser, null=False, on_delete=models.CASCADE)
    notifications = models.CharField(max_length=256, default = "")

    def __str__(self):
        return self.agency.agencyName


