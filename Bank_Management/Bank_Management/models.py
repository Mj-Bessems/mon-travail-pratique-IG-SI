from django.db import models

class Bank_Management(models.model):
    nom=models.CharField(max_length=100)
    postnom=models.CharField(max_length=100)
    prenom=models.CharField(max_length=100)
    adresse=models.CharField(max_length=100)
    num_telephone=models.CharField(max_length=100)
    class Meta:
        db_table:"clients"
    