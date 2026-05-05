from django.db import models
from .nutritionist import Nutritionist

class Product(models.Model):
    PRODUCT_TYPE_CHOICES = [
        ('herbal', 'عشبية صحية'),
        ('tools', 'أدوات الصحة'),
        ('snacks', 'سناكات صحية'),
    ]
    
    product_id = models.AutoField(primary_key=True)

    nutritionist = models.ForeignKey(
        Nutritionist,
        on_delete=models.CASCADE,
        related_name='products',
        verbose_name='أخصائي التغذية'
    )

    name = models.CharField(max_length=255, verbose_name='اسم المنتج')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='السعر')
    quantity = models.IntegerField(verbose_name='الكمية')

    img = models.ImageField(upload_to='products/', verbose_name='الصورة')

    type = models.CharField(
        max_length=50,
        choices=PRODUCT_TYPE_CHOICES,
        verbose_name='النوع'
    )

    description = models.TextField(blank=True, verbose_name='الوصف')

    is_available = models.BooleanField(default=True, verbose_name='متاح')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'product'
        verbose_name = 'منتج'
        verbose_name_plural = 'المنتجات'
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['nutritionist']),
            models.Index(fields=['is_available']),
        ]
    
    def __str__(self):
        return self.name
