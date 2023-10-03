from django.db import models

class Musician(models.Model):
    #id = models.AutoField(Primary_Key = True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    instruments = models.CharField(max_length=30)
    
    def __str__(self):
        return self.first_name + " " + self.last_name
    
    
class Album(models.Model):
    #id = models.AutoField(Primary_Key = True)
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    release_date = models.DateField()
    
    ratings = (
        (1, "Excellent"),
        (2, "Good"),
        (3, "Not Bad"),
        (4, "Bad"),
        (5, "Worst"),
    )
    num_stars = models.IntegerField(choices=ratings)
    
    def __str__(self):
        return self.name + ", Ratings: " + str(self.num_stars)
    
    
