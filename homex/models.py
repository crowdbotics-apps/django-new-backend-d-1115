from django.db import models


class XXX(models.Model):
    "Generated Model"
    r1 = models.BigIntegerField()
    r2 = models.DecimalField(max_digits=30, decimal_places=10, blank=True, null=True,)
    r3 = models.DateTimeField(auto_now=False, auto_now_add=True, blank=True, null=True,)


# Create your models here.
