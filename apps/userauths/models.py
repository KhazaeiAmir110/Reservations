from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from shortuuid.django_fields import ShortUUIDField


class User(AbstractUser):
    full_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    phone = models.CharField(max_length=11, unique=True)

    otp = models.CharField(max_length=100, blank=True, null=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username


class Profile(models.Model):
    pid = ShortUUIDField(length=7, max_length=25, alphabet='absdefg')
    image = models.FileField(upload_to='images/profiles', blank=True, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    eitaa = models.URLField(null=True, blank=True)

    wallet = models.DecimalField(max_digits=12,decimal_places=3, default=0)
    verified = models.BooleanField(default=False)

    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return f'{self.user.username} - {self.full_name}'


# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)
#
#
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()
#
#
# post_save.connect(create_user_profile, sender=User)
# post_save.connect(save_user_profile, sender=User)
