from django.db import models
import uuid

from django.urls.base import reverse
# Create your models here.


class Shop(models.Model):
    id = models.UUIDField(  # new
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    title = models.CharField(max_length=200, null=False)
    author = models.CharField(max_length=200, null=False)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    published_year = models.IntegerField(null=False)
    description = models.TextField()
    # ImageField needs pillow to run
    cover = models.ImageField(upload_to='uploads/%Y/%m/%d')

    # meta information
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("shop_show", kwargs={"pk": self.pk})