from django.db import models
from accounts.models import CustomUser
from datetime import date

class Page(models.Model):
    author = models.ForeignKey(CustomUser, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, null=True, blank=True, )
    content = models.TextField(max_length=1200)
    publication_date = models.DateTimeField(auto_now_add=True)
    public_access = models.BooleanField(default=False)
    public_access_date = models.DateField(blank=True, null=True)
    def save(self, *args, **kwargs):
        if self.public_access_date and self.public_access_date < date.today():
            self.public_access = True
        
        super().save(*args, **kwargs)
        
# class Post(models.Model):
    