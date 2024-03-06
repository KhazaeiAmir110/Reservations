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


class Company(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    address = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100, unique=True)
    category = models.ManyToManyField(Category, related_name='companies', blank=True)
    status = models.BooleanField(default=True)
    image = models.FileField(upload_to='company/%Y/%m/')
    golden = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Companies"
        verbose_name = "Company"
        ordering = ['name']
        constraints = []


# class WorkDate(models.Model):
#     date = models.DateField()
#     company = models.ForeignKey(Company, on_delete=models.CASCADE)
#     active = models.BooleanField(default=True)
#
#
# class WorkTime(models.Model):
#     start_time = models.TimeField()
#     end_time = models.TimeField()
#     work_date = models.ForeignKey(WorkDate, on_delete=models.CASCADE)
#     active = models.BooleanField(default=True)
