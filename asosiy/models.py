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

class HMavsum(models.Model):
    hozirgi_mavsum = models.CharField(max_length=10)

    def __str__(self):
        return self.hozirgi_mavsum

    class Meta:
        verbose_name = "Hozirgi Mavsum"
        verbose_name_plural = "Hozirgi Mavsum"

class Transfer(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    eski = models.ForeignKey(Club, on_delete=models.CASCADE, related_name="sotuvlari")
    yangi = models.ForeignKey(Club, on_delete=models.CASCADE, related_name="olganlari")
    narx = models.PositiveIntegerField()
    tah_narx = models.PositiveIntegerField()
    mavsum = models.CharField(max_length=10, default="22-23")

    def __str__(self):
        return f"{self.player} >>> {self.yangi}"

    def save(self, *args, **kwargs):
        m = HMavsum.objects.last().hozirgi_mavsum
        if self.mavsum == m:
            player = self.player
            player.club = self.yangi
            player.save()
        super(Transfer, self).save(*args, **kwargs)