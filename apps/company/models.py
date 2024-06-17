from django.utils.text import slugify
from apps.userauths.models import User
from django.db import models


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
    duration = models.DurationField()
    duration_time = models.TimeField()

    company = models.ForeignKey(Company, on_delete=models.CASCADE)


class SansHolidayDateTime(models.Model):
    date = models.DateField()
    time = models.TimeField()

    company = models.ForeignKey(Company, on_delete=models.CASCADE)


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
