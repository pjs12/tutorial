from django.db import models

# Create your models here.
class Curriculum(models.Model):
    name = models.CharField(max_length=255)

    # 오버라이딩 Overriding
    def __str__(self):
        return self.name

class Store(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=10)
    phone = models.CharField(max_length=20)
    gu = models.CharField(max_length=10)
    address = models.TextField()
    menu = models.TextField()

    class Meta:
        db_table = 'store'
        managed = False