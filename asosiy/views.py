from django.shortcuts import render
from .models import *
import datetime

def home(request):
    return render(request, 'index.html')

def clubs(request):
    content = {
        'clubs' : Club.objects.all()
    }
    return render(request, 'clubs.html', content)

def about(request):
    return render(request, 'about.html')

def players(request):
    content = {
        "players" : Player.objects.all()
    }
    return render(request, 'players.html', content)

def stats(request):
    return render(request, 'stats.html')

def transfer_records(request):
    content = {
        "transfers": Transfer.objects.all()
    }
    print(content["transfers"])
    return render(request, 'stats/transfer-records.html', content)

def predictions(request):
    return render(request, 'stats/150-accurate-predictions.html')

def expenditure(request):
    return render(request, 'stats/top-50-clubs-by-expenditure-in-2021.html')

def income(request):
    return render(request, 'stats/top-50-clubs-by-income-in-2021.html')

def latest_transfers(request):
    content = {
        "transfers" : Transfer.objects.filter(mavsum = HMavsum.objects.all().order_by("-hozirgi_mavsum")[1])
    }
    print(content["transfers"])
    return render(request, 'latest-transfers.html', content)

def u_20_players(request):
    today = datetime.date.today()
    plage = today - datetime.timedelta(days=365 * 20+20//4)
    content = {
        "players" : Player.objects.filter(tugilgan_sana__gte = plage),
        "hozirgi_yil" : datetime.date.today().year
    }
    return render(request, 'U-20 players.html', content)

def tryouts(request):
    return render(request, 'tryouts.html')

def country_club(request, davlat):
    print(davlat)
    content = {
        'clubs' : Club.objects.filter(davlat = davlat),
        'country' : davlat.title()
    }
    return render(request, 'england.html', content)

def transfer_archive(request):
    return render(request, 'transfer-archive.html')

def club_player(request, club):
    content = {
        'club' : club,
        "players" :  Player.objects.filter(club__nom = club)
    }
    return render(request, 'club_player.html', content)
