from django.db import models


class Region(models.Model):
    name = models.CharField(max_length=22)


class District(models.Model):
    name = models.CharField(max_length=30)
    region = models.ForeignKey('apps.Region', models.DO_NOTHING, null=True)
