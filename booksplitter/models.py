from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class WD_Property(models.Model):
    qid = models.CharField(max_length=12)
    category = models.ForeignKey(Category)

    def __str__(self):
        return self.qid
