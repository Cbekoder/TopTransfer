from django.contrib import admin
from .models import *

# admin.site.register(Player)
@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display =["id", 'ism', 'tugilgan_sana', 'club','davlat', 'narx', 'pozitsiya']
    list_display_links = ["id", 'ism']
    search_fields =['ism', 'club', 'davlat', 'pozitsiya']
    list_filter = ['club']
    autocomplete_fields = ['club']
    ordering = ['id', 'ism']



# admin.site.register(Club)
@admin.register(Club)
class ClubAdmin(admin.ModelAdmin):
    list_display = ['id', 'nom', 'davlat', 'presidend', 'coach']
    list_display_links = ['id', "nom"]
    list_filter = ['davlat']
    search_fields = ['nom', 'presidend', 'coach']
    ordering = ['id', 'nom']


# admin.site.register(Transfer)
@admin.register(Transfer)
class TransferAdmin(admin.ModelAdmin):
    list_display = ["id", 'player', 'eski', 'yangi', 'narx', 'mavsum']
    list_display_links = ['id', 'player']
    search_fields = ['player', 'eski', 'yangi', 'id']
    list_filter = ['mavsum']
    autocomplete_fields = ['player', 'eski', 'yangi']
    ordering = ['id', 'player']


admin.site.register(HMavsum)
