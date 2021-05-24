from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class RoadExtraction(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    uploaded_image_url = models.URLField(null=True)
    processed_image_url = models.URLField(null=True)
    date_created = models.DateTimeField(auto_now_add=True)
