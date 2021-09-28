from django.db import models

# Create your models here.


class Base(models.Model):


    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)



    class Meta:
        abstract = True


class Home(Base):



    title = models.CharField(max_length=20)
    subtitle = models.CharField(max_length=30)
    description = models.TextField(max_length=300)







