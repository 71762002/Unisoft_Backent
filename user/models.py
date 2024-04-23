from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.base_user import  BaseUserManager
from rest_framework_simplejwt.tokens import RefreshToken


from user.constant import DefaultAbstract




#--------------------------#
#      User Manager        #
#__________________________#
class UsManager(BaseUserManager):
    def create_user(self, email, password, role, is_staff=False, is_active=True, **extra_fields):
        if not email:
            raise ValueError("The given must be set")
     
        user = self.model(email=email, role=role, is_staff=is_staff, is_active=is_active, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    
    def create_superuser(self, email, password, role, **extra_fields):
        return self.create_user(email, password, role, is_staff=True, is_superuser=True, **extra_fields)


#-----------------#
#      User       #
#_________________#
class User(AbstractBaseUser,  PermissionsMixin, DefaultAbstract):
    ROLE = (
            ('admin', 'admin'),
            ('manager', 'manager'),
            ('operator', 'operator')
        )

    email = models.EmailField(max_length=200, unique=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    role = models.CharField(max_length=8, choices=ROLE, default=ROLE[1][0])
    is_staff = models.BooleanField('Staff', default=True)
    is_active = models.BooleanField('Active', default=True)
    is_superuser = models.BooleanField(default=False)


    def __str__(self) -> str:
        return  f"{self.email} - {self.first_name}"


    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {
            'refresh':str(refresh),
            'access' :str(refresh.access_token)
        }

    objects = UsManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name", "role"]


