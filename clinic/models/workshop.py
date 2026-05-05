from django.db import models
from .nutritionist import Nutritionist   

class Workshop(models.Model):
    STATUS_CHOICES = [
        ('upcoming', 'قادمة'),
        ('ongoing', 'جارية'),
        ('completed', 'اكتملت'),
        ('cancelled', 'ملغاة'),
    ]
    
    TYPE_CHOICES = [
        ('online', 'أونلاين'),
        ('in-person', 'حضوري'),
    ]
    
    workshop_id = models.AutoField(primary_key=True)

    # ← تصحيح اسم الحقل والكلاس
    nutritionist = models.ForeignKey(
        Nutritionist,
        on_delete=models.CASCADE,
        related_name='workshops',
        verbose_name='أخصائي التغذية'
    )

    title = models.CharField(max_length=255, verbose_name='العنوان')
    date = models.DateField(verbose_name='التاريخ')
    time = models.TimeField(verbose_name='الوقت')
    place = models.CharField(max_length=255, blank=True, verbose_name='المكان')
    type = models.CharField(max_length=20, choices=TYPE_CHOICES, verbose_name='النوع')
    overview = models.TextField(verbose_name='النبذة')
    img = models.ImageField(upload_to='workshops/', blank=True, null=True, verbose_name='الصورة')
    link = models.URLField(blank=True, null=True, verbose_name='الرابط')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='upcoming', verbose_name='الحالة')
    num_participants = models.IntegerField(default=0, verbose_name='عدد المشاركين')
    max_participants = models.IntegerField(null=True, blank=True, verbose_name='الحد الأقصى للمشاركين')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'workshop'
        verbose_name = 'ورشة عمل'
        verbose_name_plural = 'ورش العمل'
        ordering = ['-date', '-time']
        indexes = [
            models.Index(fields=['nutritionist', 'date']),  # ← تصحيح هنا أيضًا
            models.Index(fields=['status']),
        ]
    
    def __str__(self):
        return self.title
