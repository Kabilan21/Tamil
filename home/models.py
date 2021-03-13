from django.db import models

# Create your models here.


class Literature(models.Model):
    url = models.URLField(max_length=256, blank=False)
    data = models.CharField(max_length=50240, blank=False)

    def __str__(self):
        return f"{self.url}"
