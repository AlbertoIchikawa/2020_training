from django.db import models


# Create your models here.
class User(models.Model):
    id_user = models.IntegerField(primary_key=True)
    name = models.CharField('name', max_length=60)
    email = models.CharField('email', max_length=255)
    password = models.CharField('password', max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'user'
