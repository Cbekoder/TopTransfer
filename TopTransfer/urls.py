from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

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
    path('countries/<str:davlat>/', country_club),
    path('club_player/<str:club>/', club_player),
    path('season/<str:tm>/', season),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
