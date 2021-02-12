from django.db import models


# Create your models here.
class Product(models.Model):
    productid = models.CharField(max_length=10 )
    userid = models.CharField(max_length=10)
    profilename = models.CharField(max_length=100)
    helpfulness = models.CharField(max_length=3)
    score = models.FloatField()
    time = models.BigIntegerField()
    summary = models.TextField(max_length=100)
    text = models.TextField(max_length=100)

    def __str__(self):
        return self.productid

    def get_summary(self):
        return self.summary

    def get_text(self):
        return self.text

    def get_helpfulness(self):
        return self.helpfulness

    def get_score(self):
        return self.score
