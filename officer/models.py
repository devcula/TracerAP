from django.db import models
from PHC.models import PHC
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Officer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    access_level = models.ForeignKey(
        PHC, verbose_name="Access_PHC", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_officer(sender, instance, created, **kwargs):
    if created:
        Officer.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_officer(sender, instance, **kwargs):
    instance.officer.save()


# class MyOfficerManager(BaseUserManager):
#     def create_user(self, email, username, password,access_level):
#         if not email:
#             raise ValueError('Users must have an email address')
#         if not username:
#             raise ValueError('Users must have a username')

#         user = self.model(
#             email=self.normalize_email(email),
#             username=username,
#             password=password,
#             access_level = access_level,
#         )

#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, email, username, password):
#         user = self.create_user(
#             email=self.normalize_email(email),
#             password=password,
#             username=username,
#             access_level = None,
#         )
#         user.set_password(password)
#         user.is_admin = True
#         user.is_staff = True
#         user.is_superuser = True
#         user.save(using=self._db)
#         return user


# class Officer(AbstractBaseUser):
#     email = models.EmailField(verbose_name="email", max_length=60, unique=True)
#     username = models.CharField(max_length=30, unique=True)
#     date_joined = models.DateTimeField(
#         verbose_name='date joined', auto_now_add=True)
#     last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
#     access_level = models.ForeignKey(PHC, verbose_name="Access_PHC", on_delete=models.CASCADE,null = True,blank = True)
#     is_admin = models.BooleanField(default=False)
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=True)
#     is_superuser = models.BooleanField(default=False)
#     USERNAME_FIELD = 'username'
#     REQUIRED_FIELDS = ['email']
#     objects = MyOfficerManager()

#     def __str__(self):
#         return self.username
#     # For checking permissions. to keep it simple all admin have ALL permissons

#     def has_perm(self, perm, obj=None):
#         return self.is_admin
#     # Does this user have permission to view this app? (ALWAYS YES FOR SIMPLICITY)

#     def has_module_perms(self, app_label):
#         return True

#     def Access_Level(self):
#         return self.access_level
