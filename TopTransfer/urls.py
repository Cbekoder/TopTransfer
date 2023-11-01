from django.contrib import admin
from django.urls import path

from asosiy.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('clubs/', clubs),
    path('about/', about),
    path('players/', players),
    path('stats/', stats),
    path('stats/transfer-records/', transfer_records),
    path('stats/predictions/', transfer_records),
    path('stats/top-clubs-by-expenditure/', expenditure),
    path('stats/top-clubs-by-income/', income),
    path('latest-transfers/', latest_transfers),
    path('U20-players/', u_20_players),
    path('tryouts/', tryouts),
    path('transfer-archive/', transfer_archive),
    path('countries/england/', england),
]
