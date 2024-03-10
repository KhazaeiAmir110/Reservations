from django.utils.safestring import mark_safe
from django.utils.text import slugify
from apps.userauths.models import User
from django.db import models
from django.urls import reverse


class Category(models.Model):
    sub_category = models.ForeignKey('self', on_delete=models.CASCADE, related_name='scategory',
                                     null=True, blank=True)
    is_subb = models.BooleanField(default=False)
    name = models.CharField(max_length=50)
    slug = models.SlugField()
    status = models.BooleanField(default=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home:category_filter', args=[self.slug])


STATUS_CHOICES = (
    ('pending', 'Pending'),
    ('approved', 'Approved'),
    ('rejected', 'Rejected')
)


class Company(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    address = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100, unique=True)
    category = models.ManyToManyField(Category, related_name='companies')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    image = models.FileField(upload_to='company/%Y/%m/', blank=True)
    golden = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.slug == "" or self.slug is None:
            self.slug = slugify(self.name) + '-' + str(self.user)
        super(Company, self).save(*args, **kwargs)

    def thumbnail(self):
        return mark_safe("<img src='/static' width='100' height='100' style='object-fit:cover; border-radius:6px' />")

    def company_count(self):
        return Company.objects.all()

    class Meta:
        verbose_name_plural = "Companies"
        verbose_name = "Company"
        ordering = ['name']
        constraints = []


class WorkDate(models.Model):
    date = models.DateField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)

    def count_date(self):
        return WorkDate.objects.filter(company=self.company, active=True).count()


class WorkTime(models.Model):
    start_time = models.TimeField()
    end_time = models.TimeField()
    work_date = models.ForeignKey(WorkDate, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)

    def count_time(self):
        return WorkTime.objects.filter(work_date=self.work_date, active=True).count()


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=11)

    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    payment_status = models.BooleanField(default=False)

    work_date = models.ForeignKey(WorkDate, on_delete=models.CASCADE)
    work_time = models.ForeignKey(WorkTime, on_delete=models.CASCADE)

    active = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return f"{self.full_name} - {self.company} - {self.active}"
