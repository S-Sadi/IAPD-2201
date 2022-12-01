from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=30, null=False, blank=False)
    slug = models.SlugField(max_length=10, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=30, null=False, blank=False)
    price = models.FloatField()
    image = models.ImageField(upload_to='ProdImage')
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
