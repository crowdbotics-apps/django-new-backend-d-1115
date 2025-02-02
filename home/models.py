from django.db import models

# Create your models here.

from django.db import models


class CustomText(models.Model):
    title = models.CharField(max_length=150,)
    r2 = models.DecimalField(null=True, blank=True, max_digits=30, decimal_places=10,)

    def __str__(self):
        return self.title

    @property
    def api(self):
        return f"/api/v1/customtext/{self.id}/"

    @property
    def field(self):
        return "title"


class HomePage(models.Model):
    body = models.TextField()

    @property
    def api(self):
        return f"/api/v1/homepage/{self.id}/"

    @property
    def field(self):
        return "body"


class R1(models.Model):
    "Generated Model"
    r1 = models.BigIntegerField()
    r2 = models.BigIntegerField(null=True, blank=True,)


class R2(models.Model):
    "Generated Model"
    r1 = models.BigIntegerField()
    r3 = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="r2_r3",
    )


class R3(models.Model):
    "Generated Model"
    r1 = models.ForeignKey(
        "home.CustomText", on_delete=models.CASCADE, related_name="r3_r1",
    )
    r2 = models.ForeignKey(
        "home.HomePage", on_delete=models.CASCADE, related_name="r3_r2",
    )
    r3 = models.ForeignKey("home.R1", on_delete=models.CASCADE, related_name="r3_r3",)
    r4 = models.ForeignKey("home.R2", on_delete=models.CASCADE, related_name="r3_r4",)
    r5 = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="r3_r5",
    )
    r6 = models.CharField(max_length=26,)


class R4(models.Model):
    "Generated Model"
    r1 = models.BigIntegerField()
    r2 = models.DecimalField(null=True, blank=True, max_digits=30, decimal_places=10,)
    r3 = models.DateTimeField(
        null=True, blank=True, auto_now=False, auto_now_add=False,
    )
    r4 = models.DecimalField(null=True, blank=True, max_digits=30, decimal_places=10,)
    r5 = models.ForeignKey(
        "home.TGGGG",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="r4_r5",
    )


class R6(models.Model):
    "Generated Model"
    r2 = models.BigIntegerField()
    r1 = models.BigIntegerField(null=True, blank=True,)
    r3 = models.DecimalField(null=True, blank=True, max_digits=30, decimal_places=10,)
    r4 = models.DateTimeField(null=True, blank=True, auto_now=False, auto_now_add=True,)


class BVVVV(models.Model):
    "Generated Model"
    r1 = models.BigIntegerField()
    r2 = models.OneToOneField(
        "home.FRFRFR",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="bvvvv_r2",
    )


class GGGG(models.Model):
    "Generated Model"
    r1 = models.BigIntegerField()
    r2 = models.ManyToManyField(
        "home.R4", null=True, blank=True, related_name="gggg_r2",
    )
    r3 = models.ForeignKey(
        "home.R1",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="gggg_r3",
    )
    r4 = models.OneToOneField(
        "home.R2",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="gggg_r4",
    )


class TGGGG(models.Model):
    "Generated Model"
    r1 = models.BigIntegerField()
    r2 = models.OneToOneField(
        "home.R6",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="tgggg_r2",
    )


class Gffff(models.Model):
    "Generated Model"
    r1 = models.BigIntegerField()
    r2 = models.OneToOneField(
        "home.R1",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="gffff_r2",
    )


class FRFRFR(models.Model):
    "Generated Model"
    r1 = models.BigIntegerField()
