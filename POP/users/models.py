from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser, BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, email, username, password=None, user_type='user', **extra_fields):
        if not email: 
            raise ValueError('Please fill out the Email Field')
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, user_type=user_type **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, username, password=None, **extra_fields):
        extra_fields.setdefault('is_admin', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_admin') is not True:
            raise ValueError('Superuser must have is_admin=True')
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True')
        
        return self.create_user(email, username, password, **extra_fields)

class User(AbstractBaseUser):
    USER_TYPES = [
        ('admin', 'Admin'),
        ('user', 'User')
    ]

    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.EmailField(max_length=25, unique=True)
    phone = models.CharField(max_length=25)
    address = models.CharField(max_length=25)
    zip = models.CharField(max_length=5)
    user_type = models.CharField(max_length=5, choices=USER_TYPES, default='user')
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    password = models.CharField(max_length=125)

    objects = UserManager() # This tells Django to use UserManager as the default manager for this custom user model.

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name', 'phone', 'address', 'zip']

    def __str__(self):
        return self.username

