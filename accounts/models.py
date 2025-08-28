from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.core.validators import FileExtensionValidator

# Create your models here.
def user_avatar_path(instance, filename):
    user_id = instance.pk if instance.pk else 'temp'
    return f'avatars/user_{user_id}/{filename}'

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('You did not entered a valid email adress.')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self.db)
        
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    avatar = models.ImageField(
        upload_to=user_avatar_path,
        default='defaults/default_avatar.png',
        validators=[FileExtensionValidator(['jpg', 'jpeg', 'png', 'gif'])],
        blank=True,
        null=True
    )
    email = models.EmailField(unique=True)
    real_name = models.CharField(max_length=50)
    user_name = models.CharField(max_length=30, unique=True)
    birthday = models.DateField(null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    objects = CustomUserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    
    def __str__(self):
        return self.email