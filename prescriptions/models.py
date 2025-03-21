from django.db import models
from persons.models import Person
from medications.models import Medication
from users.models import User

class Prescription(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='prescriptions')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='prescriptions')
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Prescription #{self.id} for {self.person.name}"

class PrescriptionItem(models.Model):
    prescription = models.ForeignKey(Prescription, on_delete=models.CASCADE, related_name='items')
    medication = models.ForeignKey(Medication, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.quantity}x {self.medication.name}"