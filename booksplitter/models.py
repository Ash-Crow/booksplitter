from django.db import models


class WD_Property(models.Model):
    qid = models.CharField(max_length=12)
    category = models.CharField(max_length=40)

    def __str__(self):
        return self.qid
