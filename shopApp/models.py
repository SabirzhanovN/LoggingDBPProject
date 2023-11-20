from accounts.models import User
from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to="photos")

    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"


class LoggingMoves(models.Model):
    time = models.DateTimeField(auto_now=True)
    ip_address = models.GenericIPAddressField()
    author = models.CharField(max_length=100)
    method = models.CharField(max_length=20)
    sql_query = models.TextField()
    path = models.URLField()
    verdict = models.CharField(max_length=15)
    email = models.EmailField(null=True)

    def __str__(self):
        return str(self.method)

    class Meta:
        verbose_name = "Logging"
        verbose_name_plural = "Loggings"
