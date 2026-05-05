from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from .clinic import Clinic

class Nutritionist(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='nutritionist_profile',
        verbose_name='حساب المستخدم'
    )

    clinic = models.ForeignKey(
        Clinic,
        on_delete=models.CASCADE,
        related_name='nutritionists',
        verbose_name='العيادة'
    )
    phone_validator = RegexValidator(
    regex=r'^\+?[1-9]\d{7,14}$',
    message="الرجاء إدخال رقم هاتف دولي صالح")



    phone = models.CharField(
    max_length=20,
    validators=[phone_validator],
    verbose_name="رقم الهاتف"
)

    specialization = models.CharField(max_length=255, verbose_name='التخصص')
    overview = models.TextField(blank=True, verbose_name='نبذة')

    profile_image = models.ImageField(
        upload_to='nutritionists/',
        blank=True,
        null=True,
        verbose_name='صورة الملف'
    )

      ## is_active = models.BooleanField(default=True, verbose_name='نشط')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'nutritionist'
        verbose_name = 'أخصائي تغذية'
        verbose_name_plural = 'أخصائيو التغذية'
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['user']),
            models.Index(fields=['clinic']),
        ]

    def __str__(self):
        return self.user.get_full_name() or self.user.username
