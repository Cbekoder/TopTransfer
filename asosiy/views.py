from django.shortcuts import render


def home(request):
    return render(request, 'index.html')

def clubs(request):
    return render(request, 'clubs.html')

def about(request):
    return render(request, 'about.html')

def players(request):
    return render(request, 'players.html')

def stats(request):
    return render(request, 'stats.html')

def transfer_records(request):
    return render(request, 'stats/transfer-records.html')

def predictions(request):
    return render(request, 'stats/150-accurate-predictions.html')

def expenditure(request):
    return render(request, 'stats/top-50-clubs-by-expenditure-in-2021.html')

def income(request):
    return render(request, 'stats/top-50-clubs-by-income-in-2021.html')

def latest_transfers(request):
    return render(request, 'latest-transfers.html')

def u_20_players(request):
    return render(request, 'U-20 players.html')

def tryouts(request):
    return render(request, 'tryouts.html')

def england(request):
    return render(request, 'england.html')

def transfer_archive(request):
    return render(request, 'transfer-archive.html')


