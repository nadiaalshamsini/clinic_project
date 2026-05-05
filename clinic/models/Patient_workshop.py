from django.db import models
from .patient import Patient
from .workshop import Workshop

class PatientWorkshop(models.Model):
    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE,
        related_name='workshop_registrations'
    )
    workshop = models.ForeignKey(
        Workshop,
        on_delete=models.CASCADE,
        related_name='participants'
    )

    class Meta:
        db_table = 'patient_workshop'
        unique_together = ('patient', 'workshop')
        verbose_name = 'اشتراك ورشة'
        verbose_name_plural = 'اشتراكات الورش'
        ordering = ['patient']
    
    def __str__(self):
        return f"{self.patient} - {self.workshop}"
