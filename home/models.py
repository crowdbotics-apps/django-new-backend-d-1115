from django.db import models

# Create your models here.

from django.db import models


class CustomText(models.Model):
    title = models.CharField(max_length=150,)

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


class R2(models.Model):
    "Generated Model"
    r1 = models.BigIntegerField()
    r2 = models.BigIntegerField()
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


class R6(models.Model):
    "Generated Model"
    r2 = models.BigIntegerField()
