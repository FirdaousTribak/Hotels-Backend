from djongo import models

# Create your models here.


class booking(models.Model):
    Image = models.TextField(max_length=100)
    Lien= models.TextField(max_length=10)
    Ville = models.TextField(max_length=50)
    Localisation = models.TextField(max_length=100)
    Position = models.TextField(max_length=50)
    Etoile_Avis=models.IntegerField()
    Avis=  models.TextField(max_length=10)
    Nbr_Experience = models.TextField(max_length=10)
    Type_Chambre = models.TextField(max_length=100)
    Type_Lit= models.TextField(max_length=50)
    Duree= models.TextField(max_length=10)
    Prix= models.TextField(max_length=10)
    Taxes= models.TextField(max_length=50)
    Periode= models.TextField(max_length=10)
    


    
    def __str__(self):
        return self.title
