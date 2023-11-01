from django.db import models

class Club(models.Model):
    nom = models.CharField(max_length=30)
    logo = models.FileField()
    davlat = models.CharField(max_length=30)
    presidend = models.CharField(max_length=40, blank = True)
    coach = models.CharField(max_length=30, blank= True)
    yili = models.DateField(blank=True)
    record_transfer = models.CharField(max_length=100, blank=True)
    record_sotuv = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.nom

class Player(models.Model):
    ism = models.CharField(max_length=30)
    davlat = models.CharField(max_length=30)
    tugilgan_sana = models.DateField(blank=True)
    narx = models.PositiveIntegerField()
    club = models.ForeignKey(Club, on_delete=models.SET_NULL, null = True)
    pozitsiya = models.CharField(max_length=30)

    def __str__(self):
        return self.ism

class Transfer(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    eski = models.ForeignKey(Player, on_delete=models.CASCADE, related_name="sotuvlari")
    yangi = models.ForeignKey(Player, on_delete=models.CASCADE, related_name="olganlari")
    narx = models.PositiveIntegerField()
    tah_narx = models.PositiveIntegerField()
    mavsum = models.CharField(max_length=10)