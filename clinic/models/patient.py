from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

class Patient(models.Model):
    GENDER_CHOICES = [
        ('male', 'ذكر'),
        ('female', 'أنثى'),
        ('other', 'آخر'),
    ]

    phone_validator = RegexValidator(
        regex=r'^\+?[1-9]\d{7,14}$',
        message="الرجاء إدخال رقم هاتف دولي صالح"
    )

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='patient_profile'
    )

    email = models.EmailField(
        verbose_name="البريد الإلكتروني",
        blank=True,
        null=True
    )

    phone = models.CharField(
        max_length=20,
        validators=[phone_validator],
        verbose_name="رقم الهاتف"
    )

    gender = models.CharField(
        max_length=10,
        choices=GENDER_CHOICES,
        verbose_name='الجنس'
    )

    birth_date = models.DateField(verbose_name='تاريخ الميلاد')

    address = models.CharField(
        max_length=255,
        verbose_name='العنوان'
    )

    height = models.FloatField(
        verbose_name="الطول"
    )

    start_weight = models.FloatField(
        verbose_name="الوزن عند البدء"
    )

    profile_image = models.ImageField(
        upload_to='patients/',
        blank=True,
        null=True,
        verbose_name='صورة الملف'
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'patient'
        verbose_name = 'مريض'
        verbose_name_plural = 'المرضى'
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['user']),
        ]

    def __str__(self):
        return self.user.get_full_name() or self.user.username
