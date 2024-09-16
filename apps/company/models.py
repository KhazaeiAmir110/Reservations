from django.db import models
from django.utils.text import slugify

from apps.userauths.models import User
from reservations.core.structs import EnumBase, EnumMember


class Company(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    address = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.slug == "" or self.slug is None:
            self.slug = slugify(self.name) + '-' + str(self.user)
        super(Company, self).save(*args, **kwargs)

    def company_count(self):
        return Company.objects.all()

    class Meta:
        verbose_name_plural = "Companies"
        verbose_name = "Company"
        ordering = ['name']
        constraints = []


class HolidaysDate(models.Model):
    date = models.DateField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE)


class SansConfig(models.Model):
    start_time = models.TimeField()
    end_time = models.TimeField()
    duration = models.IntegerField(default=30)
    amount = models.CharField(max_length=10, default=0)

    company = models.OneToOneField(Company, on_delete=models.CASCADE)


class SansHolidayDateTime(models.Model):
    start_time = models.TimeField()
    end_time = models.TimeField()

    company = models.OneToOneField(Company, on_delete=models.CASCADE)


class Reservation(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    phone_number = models.CharField(max_length=11)
    email = models.EmailField()

    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return f"{self.first_name} - {self.last_name} - {self.company}"


class Payment(models.Model):
    class StatusEnum(EnumBase):
        SENT = EnumMember(0, 'Sent')
        PENDING = EnumMember(1, 'Pending')
        PAID = EnumMember(2, 'Paid')
        NOT_PAID = EnumMember(3, 'Not Paid')

    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)
    status = models.PositiveIntegerField(
        default=StatusEnum.SENT, choices=StatusEnum.to_tuple()
    )
