from django.db import models


# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Book(models.Model):
    status_book = [
        ('available', 'available'),
        ('rental', 'rental'),
        ('sold', 'sold'),
    ]

    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50, null=True, blank=True)
    photo_book = models.ImageField(upload_to='photos', null=True, blank=True)
    author_book = models.ImageField(upload_to='photos', null=True, blank=True)  # if you didn't add photo don't to any errors
    pages_of_book = models.IntegerField(null=True, blank=True)  # if you didn't add pages  don't to any errors
    price = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)  # if you didn't add price don't to any errors
    rental_price_day = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)  # if you didn't add price don't to any errors
    rental_preiod = models.IntegerField(null=True, blank=True)
    active = models.BooleanField(default=True)
    status = models.CharField(max_length=30, choices=status_book, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return self.title
