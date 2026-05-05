from django.db import models
from .nutritionist import Nutritionist

class Package(models.Model):
    CATEGORY_CHOICES = [
        ('medical', 'إجراءات طبية'),
        ('diet', 'حمية غذائية'),
    ]

    package_id = models.AutoField(primary_key=True)

    nutritionist = models.ForeignKey(
        Nutritionist,
        on_delete=models.CASCADE,
        related_name='packages',
        verbose_name='أخصائي التغذية'
    )

    name = models.CharField(max_length=255, verbose_name='اسم الباقة')
    details = models.TextField(verbose_name='مميزات الباقة')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='سعر الباقة')

    num = models.IntegerField(verbose_name='مدة الباقة (بالشهور)')

    first_payment_percentage = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name='نسبة الدفعة الأولى'
    )

    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        verbose_name='نوع الباقة'
    )

    require_consultation = models.BooleanField(
        default=False,
        verbose_name='استشارة مسبقة'
    )

    status = models.BooleanField(default=True, verbose_name='نشطة')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'package'
        verbose_name = 'باقة'
        verbose_name_plural = 'الباقات'
        ordering = ['-created_at']

    def __str__(self):
        return self.name
