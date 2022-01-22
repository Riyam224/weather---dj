import gettext
from django.db import models

# Create your models here.
from django.utils.translation import gettext as _


class city(models.Model):
    name =  models.CharField(max_length=100)

    

    class Meta:
        verbose_name = _("city")
        verbose_name_plural = _("citys")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("city_detail", kwargs={"pk": self.pk})
