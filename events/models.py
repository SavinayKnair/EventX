from django.db import models
from django.contrib.auth.models import User

class Event(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event_name = models.CharField(max_length=200)
    event_date = models.DateField()
    location = models.CharField(max_length=200)
    event_type = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='events/', blank=True, null=True)
    
    is_approved = models.BooleanField(default=False) 
    is_featured = models.BooleanField(default=False) # ✅ Added this
    
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.event_name