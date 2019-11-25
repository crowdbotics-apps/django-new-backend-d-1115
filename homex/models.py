from django.db import models


class XXX(models.Model):
    "Generated Model"
    r1 = models.BigIntegerField()
    r2 = models.DecimalField(null=True, blank=True, max_digits=30, decimal_places=10,)
    r3 = models.DateTimeField(null=True, blank=True, auto_now=False, auto_now_add=True,)
    r4 = models.ForeignKey(
        "home.R6",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="xxx_r4",
    )


# Create your models here.
