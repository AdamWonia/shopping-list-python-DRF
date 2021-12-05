from django.db import models


# Create your models here.
class ShopList(models.Model):
    product = models.CharField(max_length=120)
    amount = models.IntegerField()
    bought = models.BooleanField(default=False, blank=True, null=True)

    def __str__(self):
        return self.product
