from django.db import models
from .patient import Patient
from .nutritionist import Nutritionist

class Plan(models.Model):
    plan_id = models.AutoField(primary_key=True)

    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE,
        related_name='plans',
        verbose_name='المريض'
    )

    nutritionist = models.ForeignKey(
        Nutritionist,
        on_delete=models.CASCADE,
        related_name='plans',
        verbose_name='أخصائي التغذية'
    )

    file = models.FileField(upload_to='plans/', verbose_name='الملف')

    upload_at = models.DateTimeField(auto_now_add=True, verbose_name='تاريخ الرفع')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='آخر تحديث')

    description = models.TextField(blank=True, verbose_name='الوصف')
    
    class Meta:
        db_table = 'plan'
        verbose_name = 'خطة غذائية'
        verbose_name_plural = 'الخطط الغذائية'
        ordering = ['-upload_at']
        indexes = [
            models.Index(fields=['patient', 'nutritionist']),
        ]
    
    def __str__(self):
        return f"{self.patient} - Plan"
