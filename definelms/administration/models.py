from django.db import models


class Department(models.Model):
    id               = models.AutoField(primary_key=True)
    designation      = models.CharField(max_length=200)
    def __str__(self):
        return self.name
