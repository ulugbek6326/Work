from django.db import models

# Create your models here.

class Worker(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    phone = models.CharField(max_length=14)
    job = models.CharField(max_length=25, 
                            choices=[
                                ('Malyarchik', 'Malyarchik'),
                                ("Quruvchi", "Quruvchi"),
                                ("Santexnik", "Santexnik"),
                                ("Elektrik", "Elektrik"),
                                ("Uy tozalovchi", "Uy tozalovchi"),
                                ("Avtomobil ustasi", "Avtomobil ustasi"),
                                ("Yuk tushuruvch", "Yuk tushuruvchi"),
                                ("Mebil yig'uvchi", "Mebel yig'uvchi"),
                                ("Akfachi", "Akfachi"),
                                ("Maishiy texnika ustasi", "Maishiy texnika ustasi"),
                            ])
    
    
class Orderer(models.Model):
    name = models.CharField(max_length=25)
    surname = models.CharField(max_length=25)
    phone = models.CharField(max_length=14)