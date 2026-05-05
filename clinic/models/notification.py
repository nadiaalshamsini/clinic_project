from django.db import models
from .patient import Patient

class Notification(models.Model):
    STATUS_CHOICES = [
        ('unread', 'غير مقروءة'),
        ('read', 'مقروءة'),
        ('archived', 'مؤرشفة'),
    ]
    
    notification_id = models.AutoField(primary_key=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='notifications', verbose_name='المريض')
    title = models.CharField(max_length=255, verbose_name='العنوان')
    info = models.TextField(verbose_name='المعلومات')
    time = models.DateTimeField(auto_now_add=True, verbose_name='الوقت')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='unread', verbose_name='الحالة')
    
    class Meta:
        db_table = 'notification'
        verbose_name = 'إشعار'
        verbose_name_plural = 'الإشعارات'
        ordering = ['-time']
        indexes = [
            models.Index(fields=['patient', 'status']),
        ]
    
    def __str__(self):
        return f"{self.patient} - {self.title}"