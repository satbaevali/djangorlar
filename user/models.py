from django.db import models

from django.contrib.auth.models import (
    AbstractUser,PermissionsMixin,BaseUserManager
)

from django.utils import timezone
Department_choices=(
    ('IT','IT'),
    ('HR','HR'),
    ('Sales','Sales'),
    ('Finance','Finance'),
)
Role_choices=(
    ('Admin','Admin'),
    ('Manager','Manager'),
    ('Employee','Employee'),
)
class CustomUserManager(BaseUserManager):
    use_in_migrations = True
    def _create_user(self,username,email,password,**extra_fields):
        if not email:
            raise ValueError('The given email must be set')
        email=self.normalize_email(email)
        user=self.model(username=username,email=email,**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_user(self,username,email=None,password=None,**extra_fields):
        extra_fields.setdefault('is_staff',False)
        extra_fields.setdefault('is_superuser',False)
        return self._create_user(username,email,password,**extra_fields)
        if username is None:
            username = email.split('@')[0]  
        return self._create_user(email,username,password,**extra_fields)
    
    def create_superuser(self,username,email=None,password=None,**extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        if username is None:
            username = email.split('@')[0]
        return self._create_user(username,email,password,**extra_fields)
class CustomUser(AbstractUser,PermissionsMixin):
    email=models.EmailField(unique=True)
    username = models.CharField(max_length=150, unique=True)
    first_name=models.CharField(max_length=30,blank=True)
    last_name=models.CharField(max_length=30,blank=True)
    phone = models.CharField(max_length=15,blank=True)
    city = models.CharField(max_length=50,blank=True)
    country = models.CharField(max_length=50,blank=True)
    department = models.CharField(max_length=50,choices=Department_choices,blank=True)
    role = models.CharField(max_length=50,choices=Role_choices,blank=True)
    birth_date = models.DateField(null=True, blank=True)
    salary = models.IntegerField(null=True, blank=True)
  

    #standard fields
    
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(null=True, blank=True)

    objects = CustomUserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}".strip()
    
    def get_short_name(self):
        return self.first_name or self.username
    
    def __str__(self):
        return self.email+" ("+self.username+")"+" - "+self.role +" in "+self.department + self.city+", "+self.country