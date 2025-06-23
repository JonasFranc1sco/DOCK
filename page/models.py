from django.db import models
from accounts.models import CustomUser

class Page(models.Model):
    author = models.ForeignKey(CustomUser, null=True, on_delete=models.CASCADE)
    content = models.TextField(max_length=900)
    publication_date = models.DateTimeField(auto_now_add=True)
    public_access = models.BooleanField(default=False)