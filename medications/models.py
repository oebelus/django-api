from django.db import models

class Medication(models.Model):
    name = models.CharField(max_length=100)
    dosage = models.CharField(max_length=50)
    manufacturer = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} ({self.dosage})"