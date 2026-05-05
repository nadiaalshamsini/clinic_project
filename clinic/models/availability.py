from django.db import models
from .clinic import Clinic
from .nutritionist import Nutritionist

class Availability(models.Model):
    DAYS_CHOICES = [
        ('saturday', 'السبت'),
        ('sunday', 'الأحد'),
        ('monday', 'الإثنين'),
        ('tuesday', 'الثلاثاء'),
        ('wednesday', 'الأربعاء'),
        ('thursday', 'الخميس'),
        ('friday', 'الجمعة'),
    ]
    
    availability_id = models.AutoField(primary_key=True)

    clinic = models.ForeignKey(
        Clinic,
        on_delete=models.CASCADE,
        related_name='availabilities',
        verbose_name='العيادة'
    )

    nutritionist = models.ForeignKey(
        Nutritionist,
        on_delete=models.CASCADE,
        related_name='availabilities',
        verbose_name='أخصائي التغذية'
    )

    day = models.CharField(max_length=20, choices=DAYS_CHOICES, verbose_name='اليوم')
    is_open = models.BooleanField(default=False, verbose_name='مفتوح')
    start_time = models.TimeField(verbose_name='وقت البداية', null=True, blank=True)
    end_time = models.TimeField(verbose_name='وقت الإغلاق')
    online_start_time = models.TimeField(null=True, blank=True, verbose_name='بداية الخدمة الأونلاين')
    online_end_time = models.TimeField(null=True, blank=True, verbose_name='نهاية الخدمة الأونلاين')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'availability'
        verbose_name = 'التوفرية'
        verbose_name_plural = 'التوفريات'
        unique_together = ('clinic', 'nutritionist', 'day')   # ← تصحيح
        indexes = [
            models.Index(fields=['clinic', 'nutritionist']),  # ← تصحيح
            models.Index(fields=['day']),
        ]
    
    def __str__(self):
        return f"{self.nutritionist} - {self.day}"   # ← تصحيح
