from django.utils import timezone
from django.db import models

class UserProfile(models.Model):
    GENDER_CHOICES = [('M', 'Male'), ('F', 'Female')]
    telegram_id = models.IntegerField(unique=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    pairing_attempts = models.PositiveIntegerField(default=0)
    is_premium = models.BooleanField(default=False)
    premium_expiry_date = models.DateTimeField(null=True, blank=True)
    def is_subscription_active(self):
        return self.is_premium and self.premium_expiry_date > timezone.now()
    
    def __str__(self):
        return f"User {self.telegram_id}"