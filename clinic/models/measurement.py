from django.db import models
from .patient import Patient
class Measurement(models.Model):
    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE,
        related_name="measurements",
        verbose_name="المريض"
    )

    date = models.DateField(verbose_name="تاريخ القياس")

    weight = models.FloatField(verbose_name="الوزن")
    waist = models.FloatField(verbose_name="الخصر")
    abdomen = models.FloatField(verbose_name="البطن")
    hip = models.FloatField(verbose_name="الورك")
    thigh = models.FloatField(verbose_name="الفخذ")
    arm = models.FloatField(verbose_name="الذراع")

    bmi = models.FloatField(verbose_name="مؤشر كتلة الجسم")

    class Meta:
        db_table = 'measurement'
        verbose_name = 'قياس'
        verbose_name_plural = 'القياسات'
        ordering = ['-date']

    def __str__(self):
        return f"قياسات {self.patient} بتاريخ {self.date}"
