from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError

from apps.userauths.models import User
from reservations.core.structs import EnumBase, EnumMember


class Company(models.Model):
    class StatusEnum(EnumBase):
        REVIEW = EnumMember(0, _('Review'))
        REJECT = EnumMember(1, _('Rejected'))
        CONFIRMED = EnumMember(2, _('Confirmed'))

    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    address = models.CharField(max_length=200)
    image = models.ImageField()
    slug = models.SlugField(max_length=100, unique=True)
    status = models.PositiveIntegerField(
        default=StatusEnum.REVIEW, choices=StatusEnum.to_tuple()
    )

    def __str__(self):
        return f"{self.name}-{self.user}"

    def save(self, *args, **kwargs):
        if self.slug == "" or self.slug is None:
            self.slug = slugify(self.name) + '-' + str(self.user)
        super(Company, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = _("Companies")
        verbose_name = _("Company")
        ordering = ['name']
        constraints = []


class HolidaysDate(models.Model):
    date = models.DateField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.company}-{self.date}"


class SansConfig(models.Model):
    start_time = models.TimeField()
    end_time = models.TimeField()
    duration = models.IntegerField(default=30)
    amount = models.IntegerField(max_length=10, default=0)

    company = models.OneToOneField(Company, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.duration}-{self.amount}"


class SansHolidayDateTime(models.Model):
    start_time = models.TimeField()
    end_time = models.TimeField()

    company = models.OneToOneField(Company, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.start_time}-{self.end_time}"


class Reservation(models.Model):
    class StatusEnum(EnumBase):
        REVIEW = EnumMember(0, _('Review'))
        REJECT = EnumMember(1, _('Rejected'))
        CONFIRMED = EnumMember(2, _('Confirmed'))

    first_name = models.CharField(max_length=100, verbose_name=_("First name"))
    last_name = models.CharField(max_length=100, verbose_name=_("Last name"))

    phone_number = models.CharField(max_length=11, verbose_name=_("Phone number"))
    email = models.EmailField(verbose_name=_("Email"))

    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    status = models.PositiveIntegerField(
        default=StatusEnum.REVIEW, choices=StatusEnum.to_tuple(), verbose_name=_("Status")
    )

    date = models.DateField(verbose_name=_("Date"))
    time = models.TimeField(verbose_name=_("Time"))

    def clean(self):
        if HolidaysDate.objects.filter(company=self.company, date=self.date).exists():
            raise ValidationError(_('Reservations cannot be made on holidays.'))

        if Reservation.objects.filter(company=self.company, date=self.date, time=self.time).exists():
            raise ValidationError(_('There is already a reservation for this date and time.'))

        try:
            sans_config = self.company.sansconfig
            if not (sans_config.start_time <= self.time <= sans_config.end_time):
                raise ValidationError(
                    _('The reservation time must be between %(start)s and %(end)s'),
                    params={'start': sans_config.start_time, 'end': sans_config.end_time},
                )

        except SansConfig.DoesNotExist:
            raise ValidationError(_('No configuration found for the company.'))

    def save(self, *args, **kwargs):
        self.clean()
        super(Reservation, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.company}"


class Payment(models.Model):
    class StatusEnum(EnumBase):
        SENT = EnumMember(0, _('Sent'))
        PENDING = EnumMember(1, _('Pending'))
        PAID = EnumMember(2, _('Paid'))
        NOT_PAID = EnumMember(3, _('Not Paid'))

    reservation = models.OneToOneField(Reservation, on_delete=models.CASCADE)
    status = models.PositiveIntegerField(
        default=StatusEnum.SENT, choices=StatusEnum.to_tuple()
    )
    code = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.reservation.date}-{self.status}"
