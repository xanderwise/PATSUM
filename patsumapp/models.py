from django.db import models

# Create your models here.
class Tel(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=20)  # ✅ New phone field
    subject = models.CharField(max_length=50)  # This now represents the selected plan
    message = models.TextField()

    def __str__(self):
        return self.name
